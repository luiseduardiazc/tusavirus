from django.urls import path
from states.views import HomeView

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
