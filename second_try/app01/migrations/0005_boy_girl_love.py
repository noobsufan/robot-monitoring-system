# Generated by Django 2.2.1 on 2019-07-14 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20190712_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Girl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Love',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Boy')),
                ('g', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Girl')),
            ],
        ),
    ]
