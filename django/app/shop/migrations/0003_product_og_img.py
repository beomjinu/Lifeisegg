# Generated by Django 4.2.2 on 2023-07-01 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_post_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='og_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]