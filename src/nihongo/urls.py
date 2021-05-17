"""nihongo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from home import views as hv

# 
urlpatterns = [
    
    #remove this
    path('admin/', admin.site.urls),

    # Function based views
    path('', hv.Index.as_view(), name='home'),
    path('hiragana/', hv.Hiragana.as_view(), name='hiragana'),
    path('katakana/', hv.Katakana.as_view(), name='katakana'),
    path('resources/', hv.Resources.as_view(), name='resources'),
    path('help/', hv.Help.as_view(), name='help'),    
    path('social/', hv.Social.as_view(), name='social'),
    path('about/', hv.About.as_view(), name='about'),
    path('terms/', hv.Terms.as_view(), name='terms'),
    path('privacy/', hv.Privacy.as_view(), name='privacy'),
    path('donate/', hv.Donate.as_view(), name='donate'),

]
