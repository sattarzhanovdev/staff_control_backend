from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Работник, Посещаемость, Бонус, Задача, Расходы
from rest_framework import generics

class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class РаботникSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    пользователь = UserShortSerializer(read_only=True)

    class Meta:
        model = Работник
        fields = [
            'id', 'пользователь',
            'имя', 'фамилия', 'год_рождения', 'график_работы', 'телефон',
            'жизни', 'бонусы', 'выполненные_задачи', 'просроченные_задачи',
            'отработанные_часы', 'зарплата', 'премия', "должность", 'тип_получения_зарплаты', 'смена', 'рабочие_дни'
        ]

class РегистрацияРаботникаSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Работник
        fields = [
            'username', 'password', 'email',
            'имя', 'фамилия', 'должность', 'год_рождения',
            'график_работы', 'телефон', 'смена', 'рабочие_дни',
            'жизни', 'бонусы', 'тип_получения_зарплаты',
            'выполненные_задачи', 'просроченные_задачи',
            'отработанные_часы', 'зарплата', 'премия'
        ]

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        email = validated_data.pop('email')

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        работник = Работник.objects.create(пользователь=user, **validated_data)
        return работник

class ПосещаемостьSerializer(serializers.ModelSerializer):
    class Meta:
        model = Посещаемость
        fields = '__all__'

class БонусSerializer(serializers.ModelSerializer):
    class Meta:
        model = Бонус
        fields = '__all__'

class ЗадачаSerializer(serializers.ModelSerializer):
    class Meta:
        model = Задача
        fields = '__all__'


class ОбновлениеЗадачиSerializer(serializers.ModelSerializer):
    class Meta:
        model = Задача
        fields = ['статус', 'потраченное_время_в_минутах', 'опоздание_по_задаче_в_минутах', 'срок']


class РасходыSerializer(serializers.ModelSerializer):
    class Meta:
        model = Расходы
        fields = '__all__'


class РасходыCreateAPIView(generics.CreateAPIView):
    queryset = Расходы.objects.all()
    serializer_class = РасходыSerializer