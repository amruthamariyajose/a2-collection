# Generated by Django 2.2 on 2022-04-28 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20220428_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categ',
            old_name='img',
            new_name='imge',
        ),
    ]