# Generated by Django 3.2.4 on 2021-06-24 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0005_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='evidence',
            field=models.FileField(default='1.png', upload_to='evidence'),
        ),
    ]