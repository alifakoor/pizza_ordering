# Generated by Django 4.0.3 on 2022-03-31 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='title',
        ),
        migrations.AddField(
            model_name='order',
            name='pizza',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pizza', to='pizza.pizza'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
