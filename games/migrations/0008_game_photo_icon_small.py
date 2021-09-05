# Generated by Django 3.2.4 on 2021-07-05 02:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_auto_20210628_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='photo_icon_small',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/%y/%m/%d/'),
            preserve_default=False,
        ),
    ]
