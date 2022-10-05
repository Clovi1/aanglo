# Generated by Django 4.1 on 2022-09-08 13:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/')),
                ('message', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='message',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
