from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from staff.views import (
    РаботникViewSet, ПосещаемостьViewSet, БонусViewSet,
    ЗадачаViewSet, РегистрацияРаботникаAPIView, МойПрофильAPIView
)

router = DefaultRouter()
router.register(r'работники', РаботникViewSet)
router.register(r'посещения', ПосещаемостьViewSet)
router.register(r'бонусы', БонусViewSet)
router.register(r'задачи', ЗадачаViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', obtain_auth_token),
    path('api/register/', РегистрацияРаботникаAPIView.as_view()),
    path('api/', include(router.urls)),
    path('api/me/', МойПрофильAPIView.as_view()),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
