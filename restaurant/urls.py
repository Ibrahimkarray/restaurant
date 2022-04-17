"""restaurant URL Configuration

The `urlpatterns` list routes URLs to viewsbyclass. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function viewsbyclass
    1. Add an import:  from my_app import viewsbyclass
    2. Add a URL to urlpatterns:  path('', viewsbyclass.home, name='home')
Class-based viewsbyclass
    1. Add an import:  from other_app.viewsbyclass import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
