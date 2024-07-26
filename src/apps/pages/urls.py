from django.urls import path

from apps.pages.views.home import HomePage


urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
]
