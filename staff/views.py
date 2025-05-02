from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Работник, Посещаемость, Бонус, Задача, Расходы
from .serializers import (
    РаботникSerializer,
    ПосещаемостьSerializer,
    БонусSerializer,
    ЗадачаSerializer,
    РегистрацияРаботникаSerializer,
    ОбновлениеЗадачиSerializer, 
    РасходыSerializer
)

class РаботникViewSet(viewsets.ModelViewSet):
    queryset = Работник.objects.all()
    serializer_class = РаботникSerializer

class ПосещаемостьViewSet(viewsets.ModelViewSet):
    queryset = Посещаемость.objects.all()
    serializer_class = ПосещаемостьSerializer

class БонусViewSet(viewsets.ModelViewSet):
    queryset = Бонус.objects.all()
    serializer_class = БонусSerializer

class ЗадачаViewSet(viewsets.ModelViewSet):
    queryset = Задача.objects.all()
    serializer_class = ЗадачаSerializer

    def get_serializer_class(self):
        if self.action in ['partial_update', 'update']:
            return ОбновлениеЗадачиSerializer
        return ЗадачаSerializer
    
class РасходыViewSet(viewsets.ModelViewSet):
    queryset = Расходы.objects.all()
    serializer_class = РасходыSerializer
    
    
class РасходыСводкаView(APIView):
    def get(self, request):
        today = timezone.now().date()
        start_week = today - timedelta(days=today.weekday())
        start_month = today.replace(day=1)

        за_день = Расход.objects.filter(дата=today).aggregate(Sum('сумма'))['сумма__sum'] or 0
        за_неделю = Расход.objects.filter(дата__gte=start_week).aggregate(Sum('сумма'))['сумма__sum'] or 0
        за_месяц = Расход.objects.filter(дата__gte=start_month).aggregate(Sum('сумма'))['сумма__sum'] or 0

        return Response({
            'за_день': за_день,
            'за_неделю': за_неделю,
            'за_месяц': за_месяц,
        })
    
class РегистрацияРаботникаAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if not request.user.is_staff:
            return Response({'error': 'Только админ может добавлять работников'}, status=403)

        serializer = РегистрацияРаботникаSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Работник успешно создан'}, status=201)
        return Response(serializer.errors, status=400)


class МойПрофильAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            работник = Работник.objects.get(пользователь=request.user)
            serializer = РаботникSerializer(работник)
            return Response(serializer.data)
        except Работник.DoesNotExist:
            return Response({'error': 'Работник не найден'}, status=404)

