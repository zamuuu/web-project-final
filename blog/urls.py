
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PagesList.as_view(), name='pages'),
    path("crear/", views.PageCreate.as_view(), name="page_create"),
    path('<int:pk>', views.PageDetail.as_view(), name='page_detail'),
    path('<int:pk>/editar', views.PageEdit.as_view(), name='page_edit'),
    path('<int:pk>/borrar', views.PageDelete.as_view(), name='page_delete'),
]
