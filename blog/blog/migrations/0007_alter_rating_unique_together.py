# Generated by Django 4.0.2 on 2022-02-14 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_averagerating_alter_post_ratingcount_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set(),
        ),
    ]
