#kopiujemy poniższe dane z todolist urls.py by nawiazac polaczenie

from django.contrib.auth import views as auth_views
from django.urls import path
from users import views
#wpisując ręcznie w przeglądarce te Path, odwołamy sie do tych podstron


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout')

]