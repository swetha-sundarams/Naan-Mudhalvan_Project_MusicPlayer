# Generated by Django 5.0.3 on 2024-04-06 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disco', '0002_songs_music'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='category_name',
            field=models.CharField(default=2, max_length=150),
            preserve_default=False,
        ),
    ]