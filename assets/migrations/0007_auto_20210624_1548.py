# Generated by Django 3.2.4 on 2021-06-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_auto_20210624_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='voucher_no',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lendmoney',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lendmoney',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='lendmoney',
            name='money_return_in_months',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='lendmoney',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='liability',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]
