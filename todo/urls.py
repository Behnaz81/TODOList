from django.urls import path
from .views import Index
from .views import Done
from .views import Delete


urlpatterns = [
    path('', Index),
    path('done/<int:id>/', Done, name='done'),
    path('delete/<int:id>/', Delete, name='delete')
]
