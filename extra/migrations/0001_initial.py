# Generated by Django 3.2 on 2022-06-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Nomi')),
                ('image', models.ImageField(upload_to='carousel/', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': 'Carousel',
                'verbose_name_plural': 'Carousel',
            },
        ),
    ]
