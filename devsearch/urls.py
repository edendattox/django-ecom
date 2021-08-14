from django.contrib import admin
from django.urls import path, include

# <str:pk>/ pk stands for primary key
# <int:pk>/ pk stands for primary key
# <slug:pk>/ pk stands for primary key


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls'))
]
