# Generated by Django 3.2.4 on 2021-07-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_blog_blogimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blogImage',
            field=models.ImageField(upload_to='photos/%y/%m/%d/'),
        ),
    ]
