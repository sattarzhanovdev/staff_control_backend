from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from staff.views import РаботникViewSet, ПосещаемостьViewSet, БонусViewSet, ЗадачаViewSet, РасходыViewSet

router = DefaultRouter()
router.register(r'работники', РаботникViewSet)
router.register(r'посещения', ПосещаемостьViewSet)
router.register(r'бонусы', БонусViewSet)
router.register(r'задачи', ЗадачаViewSet)
router.register(r'расходы', РасходыViewSet)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/', include(router.urls)),  # <-- всё ок теперь
]
