# Generated by Django 4.0.1 on 2022-01-26 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('starTeractAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='blokced',
            new_name='blocked',
        ),
    ]
