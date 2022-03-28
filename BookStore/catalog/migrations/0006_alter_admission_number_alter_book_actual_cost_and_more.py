# Generated by Django 4.0.1 on 2022-03-22 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_book_for_sale_barcode_alter_check_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='number',
            field=models.IntegerField(verbose_name='Номер поступления'),
        ),
        migrations.AlterField(
            model_name='book',
            name='actual_cost',
            field=models.IntegerField(verbose_name='Актуальная цена'),
        ),
        migrations.AlterField(
            model_name='book_for_sale',
            name='cost',
            field=models.IntegerField(verbose_name='Стоимость проданной книги'),
        ),
        migrations.AlterField(
            model_name='department',
            name='num_dep',
            field=models.IntegerField(verbose_name='Номер отдела'),
        ),
        migrations.AlterField(
            model_name='location',
            name='num_rack',
            field=models.IntegerField(verbose_name='Номер стеллажа'),
        ),
        migrations.AlterField(
            model_name='location',
            name='num_shelf',
            field=models.IntegerField(verbose_name='Номер полки'),
        ),
    ]