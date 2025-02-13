from django.urls import path
from demo import views
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [
   # Student path
   path("register/", views.student_registration, name="student_register"),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
