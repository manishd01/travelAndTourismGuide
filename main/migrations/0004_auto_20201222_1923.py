# Generated by Django 3.1.1 on 2020-12-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201221_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign_up',
            name='confirm_password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sign_up',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sign_up',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sign_up',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
