# Generated by Django 4.0.2 on 2022-02-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_rating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='averageRating',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(),
        ),
    ]