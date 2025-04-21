from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Работник(models.Model):
    пользователь = models.OneToOneField(User, on_delete=models.CASCADE)
    имя = models.CharField(max_length=100)
    фамилия = models.CharField(max_length=100)
    должность = models.CharField(max_length=255)
    год_рождения = models.IntegerField()
    график_работы = models.CharField(max_length=255)
    телефон = models.CharField(max_length=20)
    жизни = models.IntegerField(default=5)
    бонусы = models.IntegerField(default=0)
    выполненные_задачи = models.IntegerField(default=0)
    просроченные_задачи = models.IntegerField(default=0)
    отработанные_часы = models.FloatField(default=0.0)
    зарплата = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    премия = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.имя} {self.фамилия}"

class Посещаемость(models.Model):
    работник = models.ForeignKey(Работник, on_delete=models.CASCADE)
    дата = models.DateField(default=timezone.now)
    время_прихода = models.TimeField(null=True, blank=True)
    опоздание_в_минутах = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.работник.имя} {self.работник.фамилия} - {self.дата}"

class Бонус(models.Model):
    работник = models.ForeignKey(Работник, on_delete=models.CASCADE)
    дата_выдачи = models.DateField(default=timezone.now)
    описание = models.TextField()
    сумма = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Бонус для {self.работник.имя} {self.работник.фамилия} на {self.дата_выдачи}"

class Задача(models.Model):
    ПРИОРИТЕТЫ = [
        ('низкий', 'Низкий'),
        ('средний', 'Средний'),
        ('высокий', 'Высокий'),
    ]

    СТАТУСЫ = [
        ('в_ожидании', 'В ожидании'),
        ('в_процессе', 'В процессе'),
        ('выполнена', 'Выполнена'),
        ('просрочена', 'Просрочена'),
    ]

    название = models.CharField(max_length=255)
    срок = models.DateTimeField()
    приоритет = models.CharField(max_length=10, choices=ПРИОРИТЕТЫ, default='средний')
    исполнитель = models.ForeignKey(Работник, related_name='задачи', on_delete=models.CASCADE)
    постановщик = models.ForeignKey(Работник, related_name='поставленные_задачи', on_delete=models.CASCADE)
    оценка = models.IntegerField(default=0)
    потраченное_время_в_минутах = models.FloatField(default=0.0)
    статус = models.CharField(max_length=20, choices=СТАТУСЫ, default='в_ожидании')
    опоздание_по_задаче_в_минутах = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.название
