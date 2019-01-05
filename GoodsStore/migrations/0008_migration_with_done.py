# Generated by Django 2.1.4 on 2018-12-29 19:21

from django.db import migrations

def update_db(apps, schema_editor):
    Article=apps.get_model('GoodsStore','Article')

    for article in Article.objects.all():
        article.title=article.title+'____DONE'
        article.save()

class Migration(migrations.Migration):

    dependencies = [
        ('GoodsStore', '0007_auto_20181218_1339'),
    ]

    operations = [
        migrations.RunPython(update_db)
    ]
