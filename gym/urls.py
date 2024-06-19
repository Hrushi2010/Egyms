from django.urls import path
from . import views

urlpatterns = [
   # path('', views.home, name='home'),
   # path('program/<int:program_id>/', views.program_detail, name='program_detail'),
    path('', views.index, name='index'),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




