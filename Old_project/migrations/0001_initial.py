# Generated by Django 5.0.1 on 2024-01-21 12:03

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utility', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=5000)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='project.city')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('keywords', models.CharField(max_length=1000)),
                ('description', models.TextField(max_length=5000)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.city')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='project.locality')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('contact_person', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.city')),
                ('locality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.locality')),
            ],
        ),
        migrations.CreateModel(
            name='Residential_Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propert_type', models.CharField(choices=[('Residential Land', 'Residential Land'), ('Residential Apartment', 'Residential Apartment'), ('Independent House/Villa', 'Independent House/Villa'), ('Studio Apartment', 'Studio Apartment'), ('Independent/Builder Floor', 'Independent/Builder Floor'), ('Serviced Apartments', 'Serviced Apartments'), ('Farm House', 'Farm House')], max_length=25)),
                ('title', models.CharField(max_length=50)),
                ('keywords', models.CharField(max_length=255)),
                ('meta_description', models.CharField(max_length=255)),
                ('min_price', models.IntegerField(blank=True, default=0, null=True)),
                ('max_price', models.IntegerField(blank=True, default=0, null=True)),
                ('min_area', models.CharField(blank=True, max_length=50, null=True)),
                ('max_area', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(max_length=5000)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=25)),
                ('theme', models.CharField(choices=[('slider', 'slider'), ('Featured ', 'Featured'), ('Theme3', 'Theme3'), ('Theme4', 'Theme4'), ('Theme5', 'Theme5')], max_length=25)),
                ('construction_status', models.CharField(choices=[('Under Construction', 'Under Construction'), ('New Launch', 'New Launch'), ('Partially Ready To Move', 'Partially Ready To Move'), ('Ready To Move', 'Ready To Move')], max_length=25)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.city')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.developer')),
                ('locality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.locality')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='project.residential_project')),
                ('possession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utility.possession_in')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rproject_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('Residential_Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.residential_project')),
            ],
        ),
    ]
