# Generated by Django 4.2 on 2023-04-17 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Buyutmaapp', '0002_remove_savat_mahsulot_remove_savat_miqdor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='savatitem',
            name='yetkazish_puli',
            field=models.IntegerField(default=15000),
        ),
        migrations.AlterField(
            model_name='savatitem',
            name='savat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemlari', to='Buyutmaapp.savat'),
        ),
    ]
