from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path ('', views.home, name='home'),
path('add', views.ADD, name='add'),
path('edit', views.Edit, name='edit'),
path('update/<str:id>', views.update, name='update'),
path('delete/<str:id>', views.Delete, name='delete'),
   
path('register/', views.register_view, name='register'),
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
path('dash/', views.dashboard, name='dash'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)