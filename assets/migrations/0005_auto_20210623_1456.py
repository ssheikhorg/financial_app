# Generated by Django 3.2.4 on 2021-06-23 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_category_expense_income'),
    ]

    operations = [
        migrations.CreateModel(
            name='LendMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=32)),
                ('address', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=64)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('money_return_in_months', models.IntegerField()),
                ('description', models.TextField()),
                ('lend_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Liability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=11)),
                ('address', models.CharField(max_length=256)),
                ('loan_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='expense',
            options={},
        ),
        migrations.AddField(
            model_name='expense',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='expense',
            name='expense_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterOrderWithRespectTo(
            name='expense',
            order_with_respect_to=None,
        ),
    ]
