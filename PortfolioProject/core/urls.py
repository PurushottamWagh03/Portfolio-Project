from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import home, about, contact, skills, achievements, certificates, magic_load_data

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('about/', about, name='about'),
    path('projects/', include('projects.urls')),
    path('magic-load-data/', magic_load_data, name='magic_load_data'),

    path("contact/", contact, name="contact"),
    path("skills/", skills, name="skills"),
    path("achievements/", achievements, name="achievements"),
    path("certificates/", certificates, name="certificates"),

    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(next_page='home'),
        name='logout'
    ),
]

from django.views.static import serve
from django.urls import re_path

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]