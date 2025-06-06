
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import models
from .models import Watch, Category, Cart, CartItem, Order, OrderItem, Contact
from .forms import ContactForm, CheckoutForm
import json

def home(request):
    featured_watches = Watch.objects.filter(is_featured=True, is_available=True)[:3]
    hero_watch = Watch.objects.filter(is_featured=True, is_available=True).first()
    return render(request, 'ecommerce/home.html', {
        'featured_watches': featured_watches,
        'hero_watch': hero_watch,
    })

def collections(request):
    watches = Watch.objects.filter(is_available=True)
    categories = Category.objects.all()
    
    # Filter by category
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        watches = watches.filter(category=category)
    
    # Handle search functionality
    search_query = request.GET.get('q')
    if search_query:
        watches = watches.filter(
            models.Q(name__icontains=search_query) | 
            models.Q(description__icontains=search_query) | 
            models.Q(category__name__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(watches, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'ecommerce/collections.html', {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': category_slug,
    })

def watch_detail(request, slug):
    watch = get_object_or_404(Watch, slug=slug, is_available=True)
    related_watches = Watch.objects.filter(
        category=watch.category, 
        is_available=True
    ).exclude(id=watch.id)[:4]
    
    return render(request, 'ecommerce/watch_detail.html', {
        'watch': watch,
        'related_watches': related_watches,
    })

def about(request):
    return render(request, 'ecommerce/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message. We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'ecommerce/contact.html', {'form': form})

def get_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart

@require_POST
def add_to_cart(request, watch_id):
    watch = get_object_or_404(Watch, id=watch_id, is_available=True)
    cart = get_cart(request)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        watch=watch,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    if request.headers.get('Content-Type') == 'application/json':
        return JsonResponse({
            'success': True,
            'message': f'{watch.name} added to cart',
            'cart_count': cart.items.count()
        })
    
    messages.success(request, f'{watch.name} added to cart')
    return redirect('watch_detail', slug=watch.slug)

def cart_view(request):
    cart = get_cart(request)
    return render(request, 'ecommerce/cart.html', {'cart': cart})

@require_POST
def update_cart(request):
    cart = get_cart(request)
    data = json.loads(request.body)
    
    try:
        cart_item = CartItem.objects.get(cart=cart, id=data['item_id'])
        if data['quantity'] <= 0:
            cart_item.delete()
        else:
            cart_item.quantity = data['quantity']
            cart_item.save()
        
        return JsonResponse({
            'success': True,
            'cart_total': str(cart.get_total_price()),
            'item_total': str(cart_item.get_total_price()) if cart_item.id else '0'
        })
    except CartItem.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item not found'})

@require_POST
def remove_from_cart(request, item_id):
    cart = get_cart(request)
    try:
        cart_item = CartItem.objects.get(cart=cart, id=item_id)
        cart_item.delete()
        messages.success(request, 'Item removed from cart')
    except CartItem.DoesNotExist:
        messages.error(request, 'Item not found')
    
    return redirect('cart')

def checkout(request):
    cart = get_cart(request)
    if not cart.items.exists():
        messages.error(request, 'Your cart is empty')
        return redirect('cart')
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Create order
            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                postal_code=form.cleaned_data['postal_code'],
                country=form.cleaned_data['country'],
                phone=form.cleaned_data['phone'],
                total_price=cart.get_total_price()
            )
            
            # Create order items
            for cart_item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    watch=cart_item.watch,
                    price=cart_item.watch.price,
                    quantity=cart_item.quantity
                )
            
            # Clear cart
            cart.items.all().delete()
            
            messages.success(request, f'Order #{order.id} placed successfully!')
            return redirect('order_confirmation', order_id=order.id)
    else:
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'email': request.user.email,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
            }
        form = CheckoutForm(initial=initial_data)
    
    return render(request, 'ecommerce/checkout.html', {
        'form': form,
        'cart': cart,
    })

def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'ecommerce/order_confirmation.html', {'order': order})
