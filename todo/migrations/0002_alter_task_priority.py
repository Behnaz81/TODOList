# Generated by Django 5.0.7 on 2024-08-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(choices=[(1, 'خیلی مهم'), (2, 'مهم'), (3, 'متوسط'), (4, 'کم'), (5, 'خیلی کم')]),
        ),
    ]