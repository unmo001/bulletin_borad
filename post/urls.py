from django.urls import path

from post import views

app_name = 'post'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('form/', views.PostFormView.as_view(), name="form"),
    path('<int:pk>/edit/', views.TextUpdateView.as_view(), name="update"),
    path('<int:pk>/deteil/', views.UserDetailView.as_view(), name='detail')
]
