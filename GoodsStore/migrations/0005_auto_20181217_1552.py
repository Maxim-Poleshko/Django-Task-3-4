# Generated by Django 2.1.4 on 2018-12-17 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodsStore', '0004_auto_20181217_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='upload_img',
            field=models.ImageField(upload_to='image/'),
        ),
    ]