from django.urls import path
from .views import Index
from .views import Done


urlpatterns = [
    path('', Index),
    path('done/<int:id>/', Done, name='done'),
]
