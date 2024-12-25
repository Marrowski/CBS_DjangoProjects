# Generated by Django 5.1.3 on 2024-12-25 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_userprofile_user_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image_category',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_percent',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]