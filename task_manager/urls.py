
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404
handler404 = 'task.views.error_404'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("task.urls")),
]
