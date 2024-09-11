from django.contrib import admin
from django.urls import path
from agenda_management_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_agenda', views.create_agenda, name="create_agenda"),
    path('save', views.save_agenda, name="save_agenda"),
    path('get_agendas', views.get_agendas, name="get_agendas"),
    path('delete_agendas', views.delete_all_agendas, name="delete_agendas"),
    path('update/<int:id>/agenda', views.update_agenda, name="update_agenda"),
    path('edit/<int:id>/agenda', views.edit_agenda, name="edit_agenda"),
    path('delete/<int:id>/agenda', views.delete_agenda, name="delete_agenda"),



]
