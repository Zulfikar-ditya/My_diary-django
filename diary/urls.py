from django.urls import path

from . import views
app_name = 'diary'

urlpatterns = [
    path('add_diary/', views.add_diary, name="add_diary"),
    path('my_diary/', views.my_diary, name='my_diary'),
    path('detail/<int:diary_id>/', views.detail_my_diary, name='detail'),
    path('delete/<int:diary_id>/', views.delete_diary, name='delete'),
    path('edit/<int:diary_id>/', views.edit_diary, name='edit'),
]
