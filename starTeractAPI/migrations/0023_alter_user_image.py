# Generated by Django 4.0.1 on 2022-02-07 11:40

from django.db import migrations, models
import starTeractAPI.models


class Migration(migrations.Migration):

    dependencies = [
        ('starTeractAPI', '0022_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='images/user.jfif', max_length=3000, upload_to=starTeractAPI.models.uploadPathImage),
        ),
    ]
