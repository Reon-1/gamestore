# Generated by Django 3.2.4 on 2021-06-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_remove_game_descriptionlistone'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='descriptionListOne',
            field=models.TextField(blank=True),
        ),
    ]
