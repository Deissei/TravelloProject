# Generated by Django 4.1.7 on 2023-03-24 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('photo', models.ImageField(upload_to='photo_review/', verbose_name='Фото')),
                ('who', models.CharField(choices=[('ПТ', 'Путешественник'), ('ТР', 'Турист')], max_length=2, verbose_name='Кто вы')),
                ('raiting_num', models.IntegerField(default=0, help_text='От 1 до 5', verbose_name='Рейтинг')),
                ('message_review', models.TextField(max_length=500, verbose_name='Отвыз')),
            ],
            options={
                'verbose_name': 'Отзыв клиента',
                'verbose_name_plural': 'Отзывы клиентов',
            },
        ),
    ]
