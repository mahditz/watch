from django.core.management.base import BaseCommand
from django.utils.text import slugify
from ecommerce.models import Category, Watch 
from decimal import Decimal

class Command(BaseCommand):
    help = 'Add 50 watches across 5 categories with images from 1.jpg to 50.jpg'

    def handle(self, *args, **options):
        # Create 5 categories first
        categories_data = [
            {'name': 'Luxury', 'description': 'Premium luxury watches'},
            {'name': 'Sport', 'description': 'Sports and fitness watches'},
            {'name': 'Classic', 'description': 'Classic and traditional watches'},
            {'name': 'Smart', 'description': 'Smart and digital watches'},
            {'name': 'Diving', 'description': 'Professional diving watches'},
        ]

        categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'slug': slugify(cat_data['name']),
                    'description': cat_data['description']
                }
            )
            categories.append(category)
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # 50 watches data (10 per category)
        watches_data = [
            # Luxury watches (1-10)
            {'name': 'Royal Master Classic', 'category': 'Luxury', 'price': 2500.00, 'case_material': 'Gold', 'movement': 'Automatic', 'case_diameter': '42mm', 'description': 'Exquisite luxury timepiece with gold case and automatic movement'},
            {'name': 'Diamond Elite Prestige', 'category': 'Luxury', 'price': 5500.00, 'case_material': 'Platinum', 'movement': 'Manual', 'case_diameter': '40mm', 'description': 'Premium platinum watch with diamond accents'},
            {'name': 'Heritage Grand Complication', 'category': 'Luxury', 'price': 8900.00, 'case_material': 'Rose Gold', 'movement': 'Automatic', 'case_diameter': '44mm', 'description': 'Complex mechanical watch with multiple complications'},
            {'name': 'Imperial Crown Collection', 'category': 'Luxury', 'price': 3200.00, 'case_material': 'White Gold', 'movement': 'Automatic', 'case_diameter': '41mm', 'description': 'Elegant white gold timepiece from the Imperial collection'},
            {'name': 'Sovereign Moonphase', 'category': 'Luxury', 'price': 4750.00, 'case_material': 'Gold', 'movement': 'Automatic', 'case_diameter': '43mm', 'description': 'Luxury watch featuring moonphase complication'},
            {'name': 'Aristocrat Perpetual', 'category': 'Luxury', 'price': 6800.00, 'case_material': 'Platinum', 'movement': 'Manual', 'case_diameter': '39mm', 'description': 'Perpetual calendar watch in platinum case'},
            {'name': 'Noble Chronograph', 'category': 'Luxury', 'price': 3950.00, 'case_material': 'Rose Gold', 'movement': 'Automatic', 'case_diameter': '42mm', 'description': 'Rose gold chronograph with precision timing'},
            {'name': 'Majestic Tourbillon', 'category': 'Luxury', 'price': 12500.00, 'case_material': 'Platinum', 'movement': 'Manual', 'case_diameter': '45mm', 'description': 'Magnificent tourbillon watch in platinum'},
            {'name': 'Elite Dress Master', 'category': 'Luxury', 'price': 2890.00, 'case_material': 'Gold', 'movement': 'Automatic', 'case_diameter': '40mm', 'description': 'Sophisticated dress watch in gold case'},
            {'name': 'Prestige Grand Date', 'category': 'Luxury', 'price': 4250.00, 'case_material': 'White Gold', 'movement': 'Automatic', 'case_diameter': '41mm', 'description': 'Elegant watch with large date display'},

            # Sport watches (11-20)
            {'name': 'Pro Runner GPS', 'category': 'Sport', 'price': 450.00, 'case_material': 'Titanium', 'movement': 'Quartz', 'case_diameter': '44mm', 'water_resistance': '200m', 'description': 'GPS-enabled sports watch for runners'},
            {'name': 'Athletic Performance Tracker', 'category': 'Sport', 'price': 320.00, 'case_material': 'Aluminum', 'movement': 'Digital', 'case_diameter': '46mm', 'water_resistance': '150m', 'description': 'Advanced fitness tracking capabilities'},
            {'name': 'Marathon Elite', 'category': 'Sport', 'price': 580.00, 'case_material': 'Carbon Fiber', 'movement': 'Solar', 'case_diameter': '45mm', 'water_resistance': '300m', 'description': 'Solar-powered endurance sports watch'},
            {'name': 'Fitness Champion', 'category': 'Sport', 'price': 280.00, 'case_material': 'Plastic', 'movement': 'Digital', 'case_diameter': '42mm', 'water_resistance': '100m', 'description': 'Multi-sport fitness tracking watch'},
            {'name': 'Extreme Sports Pro', 'category': 'Sport', 'price': 720.00, 'case_material': 'Titanium', 'movement': 'Quartz', 'case_diameter': '48mm', 'water_resistance': '500m', 'description': 'Rugged watch for extreme sports'},
            {'name': 'Triathlon Master', 'category': 'Sport', 'price': 650.00, 'case_material': 'Stainless Steel', 'movement': 'Solar', 'case_diameter': '44mm', 'water_resistance': '200m', 'description': 'Specialized triathlon training watch'},
            {'name': 'Training Partner Pro', 'category': 'Sport', 'price': 380.00, 'case_material': 'Aluminum', 'movement': 'Digital', 'case_diameter': '43mm', 'water_resistance': '100m', 'description': 'Personal training companion watch'},
            {'name': 'Adventure Explorer', 'category': 'Sport', 'price': 520.00, 'case_material': 'Titanium', 'movement': 'Quartz', 'case_diameter': '46mm', 'water_resistance': '300m', 'description': 'Outdoor adventure sports watch'},
            {'name': 'Outdoor Survival', 'category': 'Sport', 'price': 480.00, 'case_material': 'Carbon Fiber', 'movement': 'Solar', 'case_diameter': '47mm', 'water_resistance': '200m', 'description': 'Survival features for outdoor enthusiasts'},
            {'name': 'Peak Performance', 'category': 'Sport', 'price': 420.00, 'case_material': 'Stainless Steel', 'movement': 'Quartz', 'case_diameter': '44mm', 'water_resistance': '150m', 'description': 'High-performance athletic watch'},

            # Classic watches (21-30)
            {'name': 'Vintage Heritage', 'category': 'Classic', 'price': 850.00, 'case_material': 'Stainless Steel', 'movement': 'Automatic', 'case_diameter': '39mm', 'description': 'Classic vintage-inspired timepiece'},
            {'name': 'Traditional Elegance', 'category': 'Classic', 'price': 1200.00, 'case_material': 'Gold Plated', 'movement': 'Manual', 'case_diameter': '38mm', 'description': 'Elegant traditional dress watch'},
            {'name': 'Timeless Classic', 'category': 'Classic', 'price': 950.00, 'case_material': 'Stainless Steel', 'movement': 'Automatic', 'case_diameter': '40mm', 'description': 'Timeless design with modern reliability'},
            {'name': 'Gentleman Choice', 'category': 'Classic', 'price': 780.00, 'case_material': 'Stainless Steel', 'movement': 'Quartz', 'case_diameter': '37mm', 'description': 'Perfect gentleman\'s dress watch'},
            {'name': 'Retro Revival', 'category': 'Classic', 'price': 1100.00, 'case_material': 'Rose Gold Plated', 'movement': 'Automatic', 'case_diameter': '41mm', 'description': 'Retro-inspired automatic watch'},
            {'name': 'Classic Dress Watch', 'category': 'Classic', 'price': 680.00, 'case_material': 'Stainless Steel', 'movement': 'Quartz', 'case_diameter': '38mm', 'description': 'Sophisticated dress watch for formal occasions'},
            {'name': 'Antique Style Master', 'category': 'Classic', 'price': 920.00, 'case_material': 'Gold Plated', 'movement': 'Automatic', 'case_diameter': '40mm', 'description': 'Antique-style watch with modern movement'},
            {'name': 'Executive Classic', 'category': 'Classic', 'price': 1350.00, 'case_material': 'Stainless Steel', 'movement': 'Automatic', 'case_diameter': '42mm', 'description': 'Executive-style classic timepiece'},
            {'name': 'Heritage Collection', 'category': 'Classic', 'price': 750.00, 'case_material': 'Rose Gold Plated', 'movement': 'Quartz', 'case_diameter': '39mm', 'description': 'Heritage-inspired classic watch'},
            {'name': 'Distinguished Gentleman', 'category': 'Classic', 'price': 890.00, 'case_material': 'Stainless Steel', 'movement': 'Automatic', 'case_diameter': '41mm', 'description': 'Distinguished classic watch for gentlemen'},

            # Smart watches (31-40)
            {'name': 'TechMaster Pro', 'category': 'Smart', 'price': 399.00, 'case_material': 'Aluminum', 'movement': 'Digital', 'case_diameter': '44mm', 'water_resistance': '50m', 'description': 'Advanced smartwatch with health monitoring'},
            {'name': 'Digital Life Companion', 'category': 'Smart', 'price': 299.00, 'case_material': 'Plastic', 'movement': 'Digital', 'case_diameter': '42mm', 'water_resistance': '30m', 'description': 'Smart companion for digital lifestyle'},
            {'name': 'Fitness Smart Tracker', 'category': 'Smart', 'price': 199.00, 'case_material': 'Silicone', 'movement': 'Digital', 'case_diameter': '40mm', 'water_resistance': '50m', 'description': 'Smart fitness tracking capabilities'},
            {'name': 'Connected Health Monitor', 'category': 'Smart', 'price': 449.00, 'case_material': 'Stainless Steel', 'movement': 'Digital', 'case_diameter': '45mm', 'water_resistance': '50m', 'description': 'Advanced health monitoring smartwatch'},
            {'name': 'Smart Sport Elite', 'category': 'Smart', 'price': 349.00, 'case_material': 'Titanium', 'movement': 'Digital', 'case_diameter': '46mm', 'water_resistance': '100m', 'description': 'Sports-focused smartwatch'},
            {'name': 'AI Assistant Watch', 'category': 'Smart', 'price': 599.00, 'case_material': 'Ceramic', 'movement': 'Digital', 'case_diameter': '43mm', 'water_resistance': '50m', 'description': 'AI-powered smart assistant watch'},
            {'name': 'Communication Hub', 'category': 'Smart', 'price': 379.00, 'case_material': 'Aluminum', 'movement': 'Digital', 'case_diameter': '42mm', 'water_resistance': '30m', 'description': 'Communication-focused smartwatch'},
            {'name': 'Health Guardian Pro', 'category': 'Smart', 'price': 529.00, 'case_material': 'Stainless Steel', 'movement': 'Digital', 'case_diameter': '44mm', 'water_resistance': '50m', 'description': 'Comprehensive health monitoring'},
            {'name': 'Smart Fashion Tech', 'category': 'Smart', 'price': 279.00, 'case_material': 'Rose Gold', 'movement': 'Digital', 'case_diameter': '38mm', 'water_resistance': '30m', 'description': 'Fashion-forward smart technology'},
            {'name': 'Premium Smart Edition', 'category': 'Smart', 'price': 699.00, 'case_material': 'Ceramic', 'movement': 'Digital', 'case_diameter': '45mm', 'water_resistance': '100m', 'description': 'Premium smartwatch with advanced features'},

            # Diving watches (41-50)
            {'name': 'Deep Sea Explorer', 'category': 'Diving', 'price': 1200.00, 'case_material': 'Stainless Steel', 'movement': 'Automatic', 'case_diameter': '44mm', 'water_resistance': '500m', 'description': 'Professional deep-sea diving watch'},
            {'name': 'Ocean Master Pro', 'category': 'Diving', 'price': 950.00, 'case_material': 'Titanium', 'movement': 'Automatic', 'case_diameter': '42mm', 'water_resistance': '300m', 'description': 'Professional diving timepiece'},
            {'name': 'Submarine Professional', 'category': 'Diving', 'price': 1450.00, 'case_material': 'Stainless Steel', 'movement': 'Automatic', 'case_diameter': '45mm', 'water_resistance': '1000m', 'description': 'Ultra-deep diving professional watch'},
            {'name': 'Aqua Sport Diver', 'category': 'Diving', 'price': 680.00, 'case_material': 'Stainless Steel', 'movement': 'Quartz', 'case_diameter': '43mm', 'water_resistance': '200m', 'description': 'Sport diving watch for recreational divers'},
            {'name': 'Professional Saturation', 'category': 'Diving', 'price': 1890.00, 'case_material': 'Titanium', 'movement': 'Automatic', 'case_diameter': '46mm', 'water_resistance': '1200m', 'description': 'Saturation diving professional watch'},
            {'name': 'Coral Reef Explorer', 'category': 'Diving', 'price': 780.00, 'case_material': 'Stainless Steel', 'movement': 'Automatic', 'case_diameter': '41mm', 'water_resistance': '300m', 'description': 'Diving watch for reef exploration'},
            {'name': 'Technical Diver Pro', 'category': 'Diving', 'price': 1150.00, 'case_material': 'Carbon Fiber', 'movement': 'Automatic', 'case_diameter': '44mm', 'water_resistance': '500m', 'description': 'Technical diving specialist watch'},
            {'name': 'Marine Chronometer', 'category': 'Diving', 'price': 1320.00, 'case_material': 'Stainless Steel', 'movement': 'Automatic', 'case_diameter': '43mm', 'water_resistance': '600m', 'description': 'Marine chronometer for professional use'},
            {'name': 'Underwater Mission', 'category': 'Diving', 'price': 890.00, 'case_material': 'Titanium', 'movement': 'Quartz', 'case_diameter': '42mm', 'water_resistance': '400m', 'description': 'Specialized underwater mission watch'},
            {'name': 'Abyss Guardian', 'category': 'Diving', 'price': 1650.00, 'case_material': 'Stainless Steel', 'movement': 'Automatic', 'case_diameter': '47mm', 'water_resistance': '1500m', 'description': 'Ultimate deep abyss diving watch'},
        ]

        # Create watches
        for i, watch_data in enumerate(watches_data, 1):
            # Find the category
            category = next(cat for cat in categories if cat.name == watch_data['category'])
            
            # Create or get the watch
            watch, created = Watch.objects.get_or_create(
                name=watch_data['name'],
                defaults={
                    'slug': slugify(watch_data['name']),
                    'category': category,
                    'description': watch_data['description'],
                    'price': Decimal(str(watch_data['price'])),
                    'image': f'watches/{i}.jpg',  # Image from 1.jpg to 50.jpg
                    'case_material': watch_data.get('case_material', 'Stainless Steel'),
                    'case_diameter': watch_data.get('case_diameter', '40mm'),
                    'movement': watch_data.get('movement', 'Automatic'),
                    'crystal': watch_data.get('crystal', 'Sapphire Crystal'),
                    'water_resistance': watch_data.get('water_resistance', '100m'),
                    'bracelet_material': watch_data.get('bracelet_material', 'Stainless Steel'),
                    'is_featured': i <= 5,  # First 5 watches are featured
                    'is_available': True,
                }
            )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created watch {i}: {watch.name} in {category.name} category with image {i}.jpg')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Watch already exists: {watch.name}')
                )

        self.stdout.write(
            self.style.SUCCESS('Successfully added 50 watches across 5 categories!')
        )