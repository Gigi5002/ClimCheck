from django.contrib import admin
from django.urls import path
from weather_app.views import home_view, weather_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Редирект на страницу погоды
    path('weather/', weather_view, name='weather_view'),
]
