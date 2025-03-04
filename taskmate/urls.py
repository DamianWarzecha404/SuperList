
from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_views.index, name='index'),  # nasza strona glowna, zwana jest tez Index
    path('todolist/', include('todolist_app.urls')),
    path('account/', include('users.urls')),
    path('contact', todolist_views.contact, name='contact'),
    path('about', todolist_views.about, name='about'),
]
