# Generated by Django 3.2.6 on 2021-11-19 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_personaldata_model_per_socialstatusunmarried'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialdata_model',
            name='FIN_ShareValue',
            field=models.DecimalField(db_index=True, decimal_places=2, default=50, max_digits=8, verbose_name='قيمة السهم'),
        ),
        migrations.AlterField(
            model_name='personaldata_model',
            name='PER_SocialStatusUnmarried',
            field=models.BooleanField(db_index=True, default=False, verbose_name='الحالة الإجتماعية -متزوج'),
        ),
    ]
