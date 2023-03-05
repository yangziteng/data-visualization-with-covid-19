# Generated by Django 2.2.6 on 2023-01-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChinaCov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cn_jwsrNum', models.IntegerField(default=0, verbose_name='cn_jwsrNum')),
                ('cn_heconNum', models.IntegerField(default=0, verbose_name='cn_heconNum')),
                ('cn_conNum', models.IntegerField(default=0, verbose_name='cn_conNum')),
                ('cn_deathNum', models.IntegerField(default=0, verbose_name='cn_deathNum')),
                ('cn_cureNum', models.IntegerField(default=0, verbose_name='cn_cureNum')),
                ('cn_addjwsrNum', models.IntegerField(default=0, verbose_name='cn_addjwsrNum')),
                ('cn_province_econNum', models.IntegerField(default=0, verbose_name='cn_province_econNum')),
                ('cn_contactNum', models.IntegerField(default=0, verbose_name='cn_contactNum')),
                ('ymd', models.CharField(max_length=100, verbose_name='ymd')),
            ],
            options={
                'verbose_name': 'ChinaCov',
                'verbose_name_plural': 'ChinaCov',
            },
        ),
        migrations.CreateModel(
            name='WorldCov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('die', models.IntegerField(default=0, verbose_name='die')),
                ('certain', models.IntegerField(default=0, verbose_name='certain')),
                ('recure', models.IntegerField(default=0, verbose_name='recure')),
                ('die_inc', models.IntegerField(default=0, verbose_name='die_inc')),
                ('recure_inc', models.IntegerField(default=0, verbose_name='recure_inc')),
                ('certain_inc', models.IntegerField(default=0, verbose_name='certain_inc')),
                ('date', models.CharField(max_length=100, verbose_name='ymd')),
            ],
            options={
                'verbose_name': 'WorldCov',
                'verbose_name_plural': 'WorldCov',
            },
        ),
    ]
