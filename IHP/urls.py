"""IHP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from HomeManagement import views as HomeManagementviews
from Registration import views as Registrationviews
from ProfileManagement import views as ProfileManagementviews
from Encode import views as Encodeviews
from Decode import views as Decodeviews

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeManagementviews.home, name="home"),
    path('registration/', Registrationviews.registrationPage, name="registration"),
    path('createprofile/', ProfileManagementviews.profileInformationPage, name="createprofile"),
    path('profile/', ProfileManagementviews.profilePage, name="profile"),
    path('encode/', Encodeviews.encodePage, name="encode"),
    path('decode/', Decodeviews.decodePage, name="decode"),
    path('showdata/', Decodeviews.showdata, name="showdata"),
    path('accounts/', include('django.contrib.auth.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)