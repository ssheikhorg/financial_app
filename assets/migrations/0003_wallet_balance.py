# Generated by Django 3.2.4 on 2021-06-21 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_wallet_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]