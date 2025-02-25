# Generated by Django 5.1.4 on 2025-01-07 06:17

import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attractions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attraction_name', models.CharField(max_length=155)),
                ('attraction_name_en', models.CharField(max_length=155, null=True)),
                ('attraction_name_ru', models.CharField(max_length=155, null=True)),
                ('attraction_name_ar', models.CharField(max_length=155, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_ar', models.TextField(null=True)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='main_image/')),
            ],
        ),
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('culture_name', models.CharField(max_length=35)),
                ('culture_name_en', models.CharField(max_length=35, null=True)),
                ('culture_name_ru', models.CharField(max_length=35, null=True)),
                ('culture_name_ar', models.CharField(max_length=35, null=True)),
                ('culture_description', models.TextField()),
                ('culture_description_en', models.TextField(null=True)),
                ('culture_description_ru', models.TextField(null=True)),
                ('culture_description_ar', models.TextField(null=True)),
                ('culture_image', models.ImageField(upload_to='culture-images')),
            ],
        ),
        migrations.CreateModel(
            name='CultureCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('culture_name', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='EventCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_name', models.CharField(max_length=55)),
                ('gallery_name_en', models.CharField(max_length=55, null=True)),
                ('gallery_name_ru', models.CharField(max_length=55, null=True)),
                ('gallery_name_ar', models.CharField(max_length=55, null=True)),
                ('gallery_image', models.ImageField(upload_to='gellery_images')),
                ('address', models.CharField(max_length=62)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_name', models.CharField(max_length=55)),
                ('home_name_en', models.CharField(max_length=55, null=True)),
                ('home_name_ru', models.CharField(max_length=55, null=True)),
                ('home_name_ar', models.CharField(max_length=55, null=True)),
                ('home_image', models.ImageField(blank=True, null=True, upload_to='home_images')),
                ('home_description', models.TextField()),
                ('home_description_en', models.TextField(null=True)),
                ('home_description_ru', models.TextField(null=True)),
                ('home_description_ar', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('name_en', models.CharField(max_length=155, null=True)),
                ('name_ru', models.CharField(max_length=155, null=True)),
                ('name_ar', models.CharField(max_length=155, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_ar', models.TextField(null=True)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='main_image/')),
                ('address', models.CharField(max_length=100)),
                ('address_en', models.CharField(max_length=100, null=True)),
                ('address_ru', models.CharField(max_length=100, null=True)),
                ('address_ar', models.CharField(max_length=100, null=True)),
                ('bedroom', models.PositiveIntegerField(default=1)),
                ('bathroom', models.PositiveIntegerField(default=1)),
                ('cars', models.PositiveIntegerField(default=1)),
                ('cars_en', models.PositiveIntegerField(default=1, null=True)),
                ('cars_ru', models.PositiveIntegerField(default=1, null=True)),
                ('cars_ar', models.PositiveIntegerField(default=1, null=True)),
                ('bikes', models.PositiveIntegerField(default=1)),
                ('bikes_en', models.PositiveIntegerField(default=1, null=True)),
                ('bikes_ru', models.PositiveIntegerField(default=1, null=True)),
                ('bikes_ar', models.PositiveIntegerField(default=1, null=True)),
                ('pets', models.PositiveIntegerField()),
                ('price_short_period', models.PositiveIntegerField()),
                ('price_medium_period', models.PositiveIntegerField()),
                ('price_long_period', models.PositiveIntegerField()),
                ('amenities', multiselectfield.db.fields.MultiSelectField(choices=[('Kitchen', 'Kitchen'), ('Air Conditioner', 'Air Conditioner'), ('Television with Netflix', 'Television with Netflix'), ('Free Wireless Internet', 'Free Wireless Internet'), ('Balcony or Patio', 'Balcony or Patio')], max_length=87)),
                ('safety_and_hygiene', multiselectfield.db.fields.MultiSelectField(choices=[('Daily Cleaning', 'Daily Cleaning'), ('Disinfections and Sterilizations', 'Disinfections and Sterilizations'), ('Fire Extinguishers', 'Fire Extinguishers'), ('Smoke Detectors', 'Smoke Detectors')], max_length=82)),
            ],
        ),
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitchen_name', models.CharField(max_length=155)),
                ('kitchen_name_en', models.CharField(max_length=155, null=True)),
                ('kitchen_name_ru', models.CharField(max_length=155, null=True)),
                ('kitchen_name_ar', models.CharField(max_length=155, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_ar', models.TextField(null=True)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='main_image/')),
                ('price', models.PositiveIntegerField()),
                ('specialized_menu', models.TextField()),
                ('meal_time', multiselectfield.db.fields.MultiSelectField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Brunch', 'Brunch'), ('Open Late', 'Open Late'), ('Drinks', 'Drinks')], max_length=46)),
                ('type_of_cafe', multiselectfield.db.fields.MultiSelectField(choices=[('Russian', 'Russian'), ('Asian', 'Asian'), ('Canadian', 'Canadian'), ('Chinese', 'Chinese'), ('European', 'European'), ('Japan', 'Japan'), ('Korean', 'Korean')], max_length=52)),
            ],
        ),
        migrations.CreateModel(
            name='PopularPlaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popular_name', models.CharField(max_length=155)),
                ('popular_name_en', models.CharField(max_length=155, null=True)),
                ('popular_name_ru', models.CharField(max_length=155, null=True)),
                ('popular_name_ar', models.CharField(max_length=155, null=True)),
                ('popular_image', models.ImageField(upload_to='popular_images')),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_ar', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=55)),
                ('region_name_en', models.CharField(max_length=55, null=True)),
                ('region_name_ru', models.CharField(max_length=55, null=True)),
                ('region_name_ar', models.CharField(max_length=55, null=True)),
                ('region_image', models.ImageField(upload_to='region_images')),
                ('region_description', models.TextField()),
                ('region_description_en', models.TextField(null=True)),
                ('region_description_ru', models.TextField(null=True)),
                ('region_description_ar', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region_Categoty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_category', models.CharField(choices=[('Chui', 'Chui'), ('Talas', 'Talas'), ('Batken', 'Batken'), ('Osh', 'Osh'), ('Naryn', 'Naryn'), ('Issyk-Kul', 'Issyk-Kul'), ('Jalal-Abad', 'Jalal-Abad')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KG')),
                ('user_picture', models.ImageField(blank=True, null=True, upload_to='user_pictures/')),
                ('from_user', models.CharField(max_length=62)),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='cover_photo/')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttractionReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Рейтинг')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('client_home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_reviews', to=settings.AUTH_USER_MODEL)),
                ('attractions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attractions_review', to='country.attractions')),
            ],
            options={
                'unique_together': {('client_home', 'comment')},
            },
        ),
        migrations.CreateModel(
            name='AttractionsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='attartions_image/')),
                ('attractions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='country.attractions')),
            ],
        ),
        migrations.CreateModel(
            name='AttractionsReviewImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='attraction_review_image/')),
                ('attractions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attraction_review_image', to='country.attractionreview')),
            ],
        ),
        migrations.CreateModel(
            name='CultureKitchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitchen_name', models.CharField(max_length=300)),
                ('kitchen_name_en', models.CharField(max_length=300, null=True)),
                ('kitchen_name_ru', models.CharField(max_length=300, null=True)),
                ('kitchen_name_ar', models.CharField(max_length=300, null=True)),
                ('kitchen_description', models.TextField()),
                ('kitchen_description_en', models.TextField(null=True)),
                ('kitchen_description_ru', models.TextField(null=True)),
                ('kitchen_description_ar', models.TextField(null=True)),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.culturecategory')),
            ],
        ),
        migrations.CreateModel(
            name='CultureKitchenImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='culture_kitchen_image/')),
                ('culture_kitchen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='culture_kitchen_image', to='country.culturekitchen')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_name', models.CharField(max_length=300)),
                ('currency_name_en', models.CharField(max_length=300, null=True)),
                ('currency_name_ru', models.CharField(max_length=300, null=True)),
                ('currency_name_ar', models.CharField(max_length=300, null=True)),
                ('currency_description', models.TextField()),
                ('currency_description_en', models.TextField(null=True)),
                ('currency_description_ru', models.TextField(null=True)),
                ('currency_description_ar', models.TextField(null=True)),
                ('currency_image', models.ImageField(upload_to='currency_images')),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.culturecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_images/')),
                ('title', models.CharField(max_length=52)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('address', models.CharField(max_length=150)),
                ('price', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_category', to='country.eventcategories')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('client_gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_reviews', to='country.gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games_name', models.CharField(max_length=300)),
                ('games_name_en', models.CharField(max_length=300, null=True)),
                ('games_name_ru', models.CharField(max_length=300, null=True)),
                ('games_name_ar', models.CharField(max_length=300, null=True)),
                ('games_description', models.TextField()),
                ('games_description_en', models.TextField(null=True)),
                ('games_description_ru', models.TextField(null=True)),
                ('games_description_ar', models.TextField(null=True)),
                ('games_image', models.ImageField(upload_to='games_images')),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.culturecategory')),
            ],
        ),
        migrations.CreateModel(
            name='HandCrafts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hand_name', models.CharField(max_length=300)),
                ('hand_name_en', models.CharField(max_length=300, null=True)),
                ('hand_name_ru', models.CharField(max_length=300, null=True)),
                ('hand_name_ar', models.CharField(max_length=300, null=True)),
                ('hand_description', models.TextField()),
                ('hand_description_en', models.TextField(null=True)),
                ('hand_description_ru', models.TextField(null=True)),
                ('hand_description_ar', models.TextField(null=True)),
                ('hand_image', models.ImageField(upload_to='hand_images')),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.culturecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_favorite', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='country.home')),
            ],
        ),
        migrations.CreateModel(
            name='HotelsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='hotel_images/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_image', to='country.hotels')),
            ],
        ),
        migrations.CreateModel(
            name='HotelsReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('client_hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_hotel', to=settings.AUTH_USER_MODEL)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_reviews', to='country.hotels')),
            ],
        ),
        migrations.CreateModel(
            name='HotelsReviewImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='hotel_review_image/')),
                ('hotel_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_review_image', to='country.hotelsreview')),
            ],
        ),
        migrations.CreateModel(
            name='KitchenImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='kitchen_images/')),
                ('kitchen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kitchen_image', to='country.kitchen')),
            ],
        ),
        migrations.CreateModel(
            name='KitchenLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('Website', models.URLField(blank=True, null=True)),
                ('email', models.CharField(max_length=60)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KG')),
                ('kitchen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kitchen', to='country.kitchen')),
            ],
        ),
        migrations.CreateModel(
            name='KitchenReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('nutrition_rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('service_rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('price_rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('atmosphere_rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('client_kitchen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('kitchen_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kitchen_reviews', to='country.kitchen')),
            ],
        ),
        migrations.CreateModel(
            name='KitchenReviewImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='kitchen_review_image/')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kitchen_review_image', to='country.kitchenreview')),
            ],
        ),
        migrations.CreateModel(
            name='NationalClothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes_name', models.CharField(max_length=300)),
                ('clothes_name_en', models.CharField(max_length=300, null=True)),
                ('clothes_name_ru', models.CharField(max_length=300, null=True)),
                ('clothes_name_ar', models.CharField(max_length=300, null=True)),
                ('clothes_description', models.TextField()),
                ('clothes_description_en', models.TextField(null=True)),
                ('clothes_description_ru', models.TextField(null=True)),
                ('clothes_description_ar', models.TextField(null=True)),
                ('clothes_image', models.ImageField(upload_to='clothes_images')),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.culturecategory')),
            ],
        ),
        migrations.CreateModel(
            name='NationalInstruments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_name', models.CharField(max_length=300)),
                ('national_name_en', models.CharField(max_length=300, null=True)),
                ('national_name_ru', models.CharField(max_length=300, null=True)),
                ('national_name_ar', models.CharField(max_length=300, null=True)),
                ('national_description', models.TextField()),
                ('national_description_en', models.TextField(null=True)),
                ('national_description_ru', models.TextField(null=True)),
                ('national_description_ar', models.TextField(null=True)),
                ('national_image', models.ImageField(upload_to='national_images')),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.culturecategory')),
            ],
        ),
        migrations.AddField(
            model_name='hotels',
            name='popular_places',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.popularplaces'),
        ),
        migrations.CreateModel(
            name='FavoriteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attractions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='country.attractions')),
                ('favorite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='country.favorite')),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='country.gallery')),
                ('popular_region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='country.popularplaces')),
            ],
        ),
        migrations.CreateModel(
            name='PopularReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, verbose_name='Рейтинг')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='country.popularreview')),
                ('popular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='popular_reviews', to='country.popularplaces')),
            ],
        ),
        migrations.AddField(
            model_name='popularplaces',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='popular_places', to='country.region'),
        ),
        migrations.AddField(
            model_name='kitchen',
            name='kitchen_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotels_region_image', to='country.region'),
        ),
        migrations.AddField(
            model_name='hotels',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotels_region', to='country.region'),
        ),
        migrations.AddField(
            model_name='attractions',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region', to='country.region'),
        ),
        migrations.AddField(
            model_name='region',
            name='region_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region', to='country.region_categoty'),
        ),
        migrations.CreateModel(
            name='RegionReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('stars', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='country.regionreview')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='country.region')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='review_images/')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_image', to='country.popularreview')),
            ],
        ),
        migrations.CreateModel(
            name='ToTry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_name', models.CharField(max_length=200)),
                ('to_name_en', models.CharField(max_length=200, null=True)),
                ('to_name_ru', models.CharField(max_length=200, null=True)),
                ('to_name_ar', models.CharField(max_length=200, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_ar', models.TextField(null=True)),
                ('first_description', models.TextField()),
                ('first_description_en', models.TextField(null=True)),
                ('first_description_ru', models.TextField(null=True)),
                ('first_description_ar', models.TextField(null=True)),
                ('second_description', models.TextField()),
                ('second_description_en', models.TextField(null=True)),
                ('second_description_ru', models.TextField(null=True)),
                ('second_description_ar', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='to_try_image/')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='What_to_try', to='country.region')),
            ],
        ),
    ]
