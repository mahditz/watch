from django.core.management.base import BaseCommand
from ecommerce.models import Watch, Category
from django.utils.text import slugify
import random

class Command(BaseCommand):
    help = 'Populate the database with 25 sample watches'

    def handle(self, *args, **options):
        # Create categories if they don't exist
        categories_data = [
            {'name': 'Luxury', 'description': 'Premium luxury timepieces'},
            {'name': 'Sport', 'description': 'Athletic and sporty watches'},
            {'name': 'Classic', 'description': 'Timeless classic designs'},
            {'name': 'Digital', 'description': 'Modern digital watches'},
            {'name': 'Vintage', 'description': 'Vintage-inspired timepieces'},
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

        # Watch data - 25 watches
        watches_data = [
            {
                'name': 'Centennial Royal Oak',
                'description': 'Elegant luxury timepiece with intricate craftsmanship and premium materials.',
                'price': 15999.99,
                'case_material': 'Rose Gold',
                'case_diameter': '42mm',
                'movement': 'Automatic',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '200m',
                'bracelet_material': 'Rose Gold',
                'is_featured': True,
            },
            {
                'name': 'Speedmaster Professional',
                'description': 'Professional racing chronograph with precision timing capabilities.',
                'price': 8999.99,
                'case_material': 'Titanium',
                'case_diameter': '44mm',
                'movement': 'Chronograph',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '300m',
                'bracelet_material': 'Titanium',
                'is_featured': True,
            },
            {
                'name': 'Explorer GMT',
                'description': 'Multi-timezone explorer watch perfect for world travelers.',
                'price': 12499.99,
                'case_material': 'Stainless Steel',
                'case_diameter': '40mm',
                'movement': 'GMT Automatic',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '100m',
                'bracelet_material': 'Stainless Steel',
                'is_featured': True,
            },
            {
                'name': 'Submariner Deep',
                'description': 'Professional diving watch with exceptional water resistance.',
                'price': 9899.99,
                'case_material': 'Stainless Steel',
                'case_diameter': '41mm',
                'movement': 'Automatic',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '500m',
                'bracelet_material': 'Stainless Steel',
            },
            {
                'name': 'Digital Pro Sport',
                'description': 'Advanced digital sports watch with multiple fitness tracking features.',
                'price': 899.99,
                'case_material': 'Carbon Fiber',
                'case_diameter': '45mm',
                'movement': 'Digital Quartz',
                'crystal': 'Mineral Crystal',
                'water_resistance': '200m',
                'bracelet_material': 'Silicone',
            },
            {
                'name': 'Heritage Classic',
                'description': 'Timeless design inspired by vintage watchmaking traditions.',
                'price': 3299.99,
                'case_material': 'Yellow Gold',
                'case_diameter': '38mm',
                'movement': 'Manual Wind',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '50m',
                'bracelet_material': 'Leather',
            },
            {
                'name': 'Aviator Pilot',
                'description': 'Aviation-inspired timepiece with oversized numerals and precision.',
                'price': 2799.99,
                'case_material': 'Stainless Steel',
                'case_diameter': '46mm',
                'movement': 'Automatic',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '100m',
                'bracelet_material': 'Leather',
            },
            {
                'name': 'Moon Phase Elite',
                'description': 'Sophisticated moon phase complication with astronomical accuracy.',
                'price': 18999.99,
                'case_material': 'Platinum',
                'case_diameter': '39mm',
                'movement': 'Automatic',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '30m',
                'bracelet_material': 'Alligator Leather',
            },
            {
                'name': 'Racing Chronograph',
                'description': 'High-performance racing chronograph with tachymeter scale.',
                'price': 4599.99,
                'case_material': 'Ceramic',
                'case_diameter': '43mm',
                'movement': 'Chronograph',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '100m',
                'bracelet_material': 'Carbon Fiber',
            },
            {
                'name': 'Dress Master',
                'description': 'Ultra-thin dress watch perfect for formal occasions.',
                'price': 5299.99,
                'case_material': 'White Gold',
                'case_diameter': '37mm',
                'movement': 'Ultra-thin Automatic',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '30m',
                'bracelet_material': 'Alligator Leather',
            },
            {
                'name': 'Field Commander',
                'description': 'Rugged military-inspired watch built for extreme conditions.',
                'price': 1899.99,
                'case_material': 'Titanium',
                'case_diameter': '44mm',
                'movement': 'Quartz',
                'crystal': 'Mineral Crystal',
                'water_resistance': '200m',
                'bracelet_material': 'Nylon NATO',
            },
            {
                'name': 'Ocean Diver Pro',
                'description': 'Professional diving watch with helium escape valve.',
                'price': 6799.99,
                'case_material': 'Stainless Steel',
                'case_diameter': '42mm',
                'movement': 'Automatic',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '600m',
                'bracelet_material': 'Stainless Steel',
            },
            {
                'name': 'Smart Connect',
                'description': 'Advanced smartwatch with health monitoring and connectivity.',
                'price': 1299.99,
                'case_material': 'Aluminum',
                'case_diameter': '41mm',
                'movement': 'Digital Smart',
                'crystal': 'Gorilla Glass',
                'water_resistance': '50m',
                'bracelet_material': 'Sport Band',
            },
            {
                'name': 'Vintage Retro',
                'description': 'Authentic vintage styling with modern reliability.',
                'price': 2199.99,
                'case_material': 'Bronze',
                'case_diameter': '39mm',
                'movement': 'Manual Wind',
                'crystal': 'Acrylic',
                'water_resistance': '100m',
                'bracelet_material': 'Vintage Leather',
            },
            {
                'name': 'Perpetual Calendar',
                'description': 'Complex perpetual calendar with multiple complications.',
                'price': 45999.99,
                'case_material': 'Platinum',
                'case_diameter': '40mm',
                'movement': 'Perpetual Calendar',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '30m',
                'bracelet_material': 'Platinum',
            },
            {
                'name': 'Fitness Tracker Pro',
                'description': 'Comprehensive fitness tracking with GPS and heart rate monitor.',
                'price': 699.99,
                'case_material': 'Polymer',
                'case_diameter': '42mm',
                'movement': 'Digital Quartz',
                'crystal': 'Mineral Crystal',
                'water_resistance': '100m',
                'bracelet_material': 'Silicone',
            },
            {
                'name': 'Yacht Master',
                'description': 'Nautical-inspired luxury watch for sailing enthusiasts.',
                'price': 13799.99,
                'case_material': 'Rose Gold',
                'case_diameter': '40mm',
                'movement': 'Automatic',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '100m',
                'bracelet_material': 'Rose Gold',
            },
            {
                'name': 'Tourbillon Master',
                'description': 'Exquisite tourbillon complication showcasing mechanical artistry.',
                'price': 89999.99,
                'case_material': 'Rose Gold',
                'case_diameter': '41mm',
                'movement': 'Tourbillon Manual',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '30m',
                'bracelet_material': 'Alligator Leather',
            },
            {
                'name': 'Urban Explorer',
                'description': 'Modern urban watch with sleek design and practical features.',
                'price': 1599.99,
                'case_material': 'Stainless Steel',
                'case_diameter': '41mm',
                'movement': 'Automatic',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '100m',
                'bracelet_material': 'Stainless Steel',
            },
            {
                'name': 'Power Reserve Elite',
                'description': 'Long power reserve automatic with 72-hour autonomy.',
                'price': 7299.99,
                'case_material': 'Titanium',
                'case_diameter': '40mm',
                'movement': 'Automatic',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '100m',
                'bracelet_material': 'Titanium',
            },
            # 5 additional watches to reach 25 total
            {
                'name': 'Arctic Explorer',
                'description': 'Extreme cold weather watch designed for polar expeditions.',
                'price': 3899.99,
                'case_material': 'Titanium',
                'case_diameter': '43mm',
                'movement': 'Automatic',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '300m',
                'bracelet_material': 'Rubber',
            },
            {
                'name': 'Skeleton Vision',
                'description': 'Open-worked dial showcasing the intricate mechanical movement.',
                'price': 11299.99,
                'case_material': 'Stainless Steel',
                'case_diameter': '42mm',
                'movement': 'Skeleton Automatic',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '50m',
                'bracelet_material': 'Leather',
            },
            {
                'name': 'Tactical Ops',
                'description': 'Military-grade tactical watch with night vision compatibility.',
                'price': 2299.99,
                'case_material': 'Carbon Fiber',
                'case_diameter': '45mm',
                'movement': 'Quartz',
                'crystal': 'Mineral Crystal',
                'water_resistance': '200m',
                'bracelet_material': 'Tactical Nylon',
            },
            {
                'name': 'Diamond Luxe',
                'description': 'Luxury timepiece adorned with premium diamonds and gemstones.',
                'price': 24999.99,
                'case_material': 'White Gold',
                'case_diameter': '36mm',
                'movement': 'Automatic',
                'crystal': 'Sapphire Crystal',
                'water_resistance': '30m',
                'bracelet_material': 'White Gold',
                'is_featured': True,
            },
            {
                'name': 'Solar Eco Drive',
                'description': 'Eco-friendly solar-powered watch with unlimited battery life.',
                'price': 1199.99,
                'case_material': 'Stainless Steel',
                'case_diameter': '40mm',
                'movement': 'Solar Quartz',
                'crystal': 'Mineral Crystal',
                'water_resistance': '100m',
                'bracelet_material': 'Stainless Steel',
            },
        ]

        # List of available watch images
        watch_images = [
            'watches/watch1.jpg', 'watches/watch2.jpg', 'watches/watch3.jpg',
            'watches/watch4.jpg', 'watches/watch5.jpg', 'watches/watch6.jpg',
            'watches/watch7.jpg', 'watches/watch8.jpg', 'watches/watch9.jpg',
            'watches/watch10.jpg', 'watches/watch11.jpg', 'watches/watch12.jpg',
            'watches/watch13.jpg', 'watches/watch14.jpg', 'watches/watch15.jpg',
            'watches/watch16.jpg', 'watches/watch17.jpg', 'watches/watch18.jpg',
            'watches/watch19.jpg', 'watches/watch20.jpg', 'watches/watch21.jpg',
            'watches/watch22.jpg', 'watches/watch23.jpg', 'watches/watch24.jpg',
            'watches/watch25.jpg'
        ]
        
        # Create watches
        for i, watch_data in enumerate(watches_data):
            # Assign category based on watch type
            if 'Digital' in watch_data['name'] or 'Smart' in watch_data['name'] or 'Fitness' in watch_data['name'] or 'Solar' in watch_data['name']:
                category = next(c for c in categories if c.name == 'Digital')
            elif 'Sport' in watch_data['name'] or 'Racing' in watch_data['name'] or 'Tactical' in watch_data['name'] or 'Field' in watch_data['name']:
                category = next(c for c in categories if c.name == 'Sport')
            elif 'Vintage' in watch_data['name'] or 'Heritage' in watch_data['name'] or 'Retro' in watch_data['name']:
                category = next(c for c in categories if c.name == 'Vintage')
            elif watch_data['price'] > 10000:
                category = next(c for c in categories if c.name == 'Luxury')
            else:
                category = next(c for c in categories if c.name == 'Classic')

            watch, created = Watch.objects.get_or_create(
                name=watch_data['name'],
                defaults={
                    'slug': slugify(watch_data['name']),
                    'category': category,
                    'description': watch_data['description'],
                    'price': watch_data['price'],
                    'case_material': watch_data['case_material'],
                    'case_diameter': watch_data['case_diameter'],
                    'movement': watch_data['movement'],
                    'crystal': watch_data['crystal'],
                    'water_resistance': watch_data['water_resistance'],
                    'bracelet_material': watch_data['bracelet_material'],
                    'is_featured': watch_data.get('is_featured', False),
                    'is_available': True,
                    'image': watch_images[i % len(watch_images)],  # Cycle through available images
                }
            )
            
            if created:
                self.stdout.write(f'Created watch: {watch.name}')
            else:
                self.stdout.write(f'Watch already exists: {watch.name}')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with 25 watches!')
        )
