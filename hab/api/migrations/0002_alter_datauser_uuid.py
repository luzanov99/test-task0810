# Generated by Django 3.2.8 on 2021-10-09 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datauser',
            name='uuid',
            field=models.CharField(max_length=120),
        ),
    ]
