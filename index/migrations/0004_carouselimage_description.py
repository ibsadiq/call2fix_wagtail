# Generated by Django 4.2.2 on 2023-06-23 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_rename_home_indexpage_carouselimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselimage',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
