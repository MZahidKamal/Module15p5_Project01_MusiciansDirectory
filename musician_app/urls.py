from django.urls import path
from .views import add_musician, edit_musician, delete_musician

urlpatterns = [
    path('musicians/add_musician/', add_musician, name='add_musician'),
    path('musicians/edit_musician/<int:musician_id>/', edit_musician, name='edit_musician'),
    path('musicians/delete_musician/<int:musician_id>/', delete_musician, name='delete_musician'),
]
