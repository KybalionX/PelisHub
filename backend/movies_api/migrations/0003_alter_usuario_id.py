# Generated by Django 3.2.3 on 2021-10-07 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_api', '0002_auto_20210909_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
