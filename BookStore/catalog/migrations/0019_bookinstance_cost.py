# Generated by Django 4.0.1 on 2022-04-03 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_remove_book_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='cost',
            field=models.IntegerField(default=0, help_text='Введите стоимость книги', null=True, verbose_name='Стоимость книги'),
        ),
    ]