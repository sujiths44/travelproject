# Generated by Django 3.2.13 on 2022-07-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=250)),
                ('picture', models.ImageField(upload_to='pic5')),
                ('descrip', models.TextField()),
            ],
        ),
    ]
