# Generated by Django 3.2.8 on 2021-10-09 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_datauser_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datauser',
            old_name='username',
            new_name='name',
        ),
    ]