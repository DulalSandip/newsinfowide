# Generated by Django 2.2.5 on 2020-05-14 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200514_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='post_image',
        ),
    ]
