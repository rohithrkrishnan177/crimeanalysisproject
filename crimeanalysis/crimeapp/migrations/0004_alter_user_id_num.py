# Generated by Django 3.2.4 on 2021-06-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0003_auto_20210621_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_num',
            field=models.CharField(default=0, max_length=20),
        ),
    ]