# Generated by Django 2.0.7 on 2018-08-11 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_auto_20180812_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='fullname',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]