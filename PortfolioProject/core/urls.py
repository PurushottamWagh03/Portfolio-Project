from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import home, about, contact, skills, achievements

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('about/', about, name='about'),
    path('projects/', include('projects.urls')),

    path("contact/", contact, name="contact"),
    path("skills/", skills, name="skills"),
    path("achievements/", achievements, name="achievements"),

    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(next_page='home'),
        name='logout'
    ),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)