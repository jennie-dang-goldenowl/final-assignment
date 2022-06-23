# Generated by Django 4.0.5 on 2022-06-21 05:02

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_category_alter_product_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='http://hinhnenhd.com/wp-content/uploads/2021/08/Tai-ngay-avt-trang-fb-moi-nhat-dep-nhat-doc-dao-12.jpg', upload_to=store.models.get_profile_image_path, verbose_name='Avatar'),
        ),
    ]
