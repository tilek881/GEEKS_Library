# Generated by Django 5.1.4 on 2025-01-09 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_book_books'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': 'Книги', 'verbose_name_plural': 'Список книг'},
        ),
    ]
