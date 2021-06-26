# Generated by Django 3.2.4 on 2021-06-24 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0013_auto_20210624_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallet',
            old_name='current_balance',
            new_name='balance',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='prev_balance',
        ),
        migrations.AlterField(
            model_name='expense',
            name='spender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.wallet'),
        ),
    ]