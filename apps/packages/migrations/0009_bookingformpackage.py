# Generated by Django 4.1.7 on 2023-03-25 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0008_package_activate_promo'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingFormPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Емаил')),
                ('checkin_date', models.DateField(verbose_name='Время заезда')),
                ('checkout_date', models.DateField(verbose_name='Проверить дату')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.package', verbose_name='Пакет')),
            ],
            options={
                'verbose_name': 'Бронирование Пакета',
                'verbose_name_plural': 'Бронирование Пакетов',
            },
        ),
    ]
