# Generated by Django 3.2.13 on 2022-07-12 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='picture',
            field=models.ImageField(upload_to='pic6'),
        ),
    ]