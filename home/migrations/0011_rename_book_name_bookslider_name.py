# Generated by Django 4.0.5 on 2022-06-21 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_bookslider_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookslider',
            old_name='book_name',
            new_name='name',
        ),
    ]
