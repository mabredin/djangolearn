# Generated by Django 4.0.1 on 2022-04-03 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_booking_bookinstance_cover_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(blank=True, help_text='Выберите жанр для книги', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='genre_book', to='catalog.genre', verbose_name='Жанр книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка книги'),
        ),
    ]
