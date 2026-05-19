from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('ll_project.accounts.urls')),
    path("", include("ll_project.learning_logs.urls", namespace="learning_logs")),
]