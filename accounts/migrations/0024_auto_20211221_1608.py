# Generated by Django 3.2.6 on 2021-12-21 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_main_menu_sub_menu'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Monthes_List_MODEL',
            new_name='Monthes_Menu_MODEL',
        ),
        migrations.AlterModelOptions(
            name='monthes_menu_model',
            options={'ordering': ['MM_MonthName']},
        ),
        migrations.RenameField(
            model_name='monthes_menu_model',
            old_name='MON_MonthName',
            new_name='MM_MonthName',
        ),
    ]
