# Generated by Django 5.2 on 2025-05-03 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_расходы_исполнитель'),
    ]

    operations = [
        migrations.AlterField(
            model_name='расходы',
            name='категория',
            field=models.CharField(choices=[('закуп', 'Закуп'), ('оплата за смену', 'Оплата за смену'), ('аванс', 'Аванс'), ('зарплата', 'Зарплата')], default='закуп', max_length=20),
        ),
    ]
