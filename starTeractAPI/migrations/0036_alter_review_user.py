# Generated by Django 4.0.1 on 2022-02-26 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('starTeractAPI', '0035_payment_alter_video_talent_alter_video_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user3', to='starTeractAPI.user'),
        ),
    ]
