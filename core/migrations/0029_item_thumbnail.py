# Generated by Django 4.0 on 2023-02-21 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_item_is_featured_item_num_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
