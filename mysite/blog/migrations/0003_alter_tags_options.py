# Generated by Django 4.1 on 2022-08-24 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_is_published_alter_post_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'Видео игры', 'verbose_name_plural': 'Видео игры'},
        ),
    ]
