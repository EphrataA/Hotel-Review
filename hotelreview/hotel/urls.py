"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from review.views import home, about, blog, contact, page, categories
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home_url"),
    path('about/', about, name="about_url"),
    path('blog/', blog, name="blog_url"),
    path('page/', page, name="page_url"),
    path('categories/',categories, name="categories_url"),
    path('contact/',contact, name="contact_url"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

