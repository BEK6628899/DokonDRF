# Generated by Django 4.2 on 2023-04-13 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy', '0003_mahsulot_sotuvchi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='izoh',
            name='reyting',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
