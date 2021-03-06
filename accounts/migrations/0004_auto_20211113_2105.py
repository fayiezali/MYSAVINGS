# Generated by Django 3.2.6 on 2021-11-13 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_personaldata_model'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personaldata_model',
            options={'ordering': ['PER_Customer']},
        ),
        migrations.CreateModel(
            name='HousingData_MODEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HOU_Region', models.CharField(db_index=True, max_length=25, verbose_name='المنطقة')),
                ('HOU_City', models.CharField(db_index=True, max_length=25, verbose_name='المدينة')),
                ('HOU_District', models.CharField(db_index=True, max_length=25, verbose_name='الحي')),
                ('HOU_HomeAddress', models.CharField(db_index=True, max_length=100, verbose_name='عنوان المنزل')),
                ('HOU_CurrentWork', models.CharField(db_index=True, max_length=100, verbose_name='العمل الحالي')),
                ('HOU_WorkAddress', models.CharField(db_index=True, max_length=100, verbose_name='عنوان العمل')),
                ('HOU_Customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='اسم المشترك')),
            ],
            options={
                'ordering': ['HOU_Customer'],
            },
        ),
        migrations.CreateModel(
            name='FinancialData_MODEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIN_ShareValue', models.DecimalField(db_index=True, decimal_places=2, max_digits=8, verbose_name='قيمة السهم')),
                ('FIN_NumberShares', models.IntegerField(db_index=True, default=1, verbose_name='عدد الأسهم')),
                ('FIN_BankName', models.CharField(db_index=True, max_length=50, verbose_name='إسم البنك')),
                ('FIN_BankAccount', models.CharField(db_index=True, max_length=50, verbose_name='الحساب البنكي - الآيبان')),
                ('FIN_MethodPaymentCash', models.BooleanField(db_index=True, default=True, verbose_name='طريقة سداد قيمة اﻷسهم _ نقدا')),
                ('FIN_MethodPaymentCheck', models.BooleanField(db_index=True, verbose_name='طريقة سداد قيمة اﻷسهم _ شيك')),
                ('FIN_MethodPaymentTransfer', models.BooleanField(db_index=True, verbose_name='طريقة سداد قيمة اﻷسهم _ حوالة')),
                ('FIN_MethodPayment', models.CharField(choices=[('CA', 'Cash'), ('CH', 'Check'), ('TR', 'Transfer')], db_index=True, default='CA', max_length=2, verbose_name='طريقة إستلام قيمة اﻷسهم')),
                ('FIN_SalaryDisbursementDate', models.DateField(db_index=True, verbose_name='تاريخ صرف الراتب')),
                ('FIN_DateShareReceived', models.DateField(db_index=True, verbose_name='تاريخ استلام اﻷسهم/المشاركات/المستحقات')),
                ('FIN_Customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='اسم المشترك')),
            ],
            options={
                'ordering': ['FIN_Customer'],
            },
        ),
    ]
