# Generated by Django 3.0.5 on 2022-12-09 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_auto_20221209_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pizza',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizzas.Pizza'),
            preserve_default=False,
        ),
    ]
