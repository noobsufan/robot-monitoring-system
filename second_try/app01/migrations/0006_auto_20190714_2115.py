# Generated by Django 2.2.1 on 2019-07-14 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_boy_girl_love'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='love',
            unique_together={('b', 'g')},
        ),
    ]