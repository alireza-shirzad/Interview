# Generated by Django 4.0.2 on 2022-02-14 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_rating_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='averageRating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='ratingCount',
            field=models.IntegerField(null=True),
        ),
    ]
