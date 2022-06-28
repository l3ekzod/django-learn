# Generated by Django 3.2 on 2022-05-25 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=255, verbose_name='Variant')),
                ('is_correct', models.BooleanField(default=False, verbose_name="To'g'ri")),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.question')),
            ],
        ),
    ]
