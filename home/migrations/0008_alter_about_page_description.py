# Generated by Django 5.0.2 on 2025-02-12 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_page',
            name='description',
            field=models.CharField(max_length=5000),
        ),
    ]
