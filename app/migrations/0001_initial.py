# Generated by Django 3.2.9 on 2022-01-04 11:26

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GreatTransformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('name_ar', models.CharField(max_length=255)),
                ('img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('name_ar', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('price_ar', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('description_ar', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PackageGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('name_ar', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('description_ar', models.CharField(max_length=255)),
                ('img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('about_us', models.TextField(max_length=8000)),
                ('about_us_ar', models.TextField(max_length=8000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('name_ar', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=500)),
                ('title_ar', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=500)),
                ('description_ar', models.TextField(max_length=500)),
                ('order', models.IntegerField(unique=True)),
                ('img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('title', models.CharField(max_length=255)),
                ('title_ar', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('description_ar', models.CharField(max_length=255)),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slider', to='app.setting')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PackageDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=255)),
                ('description_ar', models.CharField(max_length=255)),
                ('package_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_details', to='app.package')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='package',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.packagegroup'),
        ),
        migrations.CreateModel(
            name='GreatTransformationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=255)),
                ('description_ar', models.CharField(max_length=255)),
                ('trans_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trans_details', to='app.greattransformation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
