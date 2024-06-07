"""coin_scraper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from coinmanager.views import StartScrapingView, ScrapingStatusView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/coinmanager/start_scraping', StartScrapingView.as_view(), name='start_scraping'),
    path('api/coinmanager/scraping_status/<uuid:job_id>', ScrapingStatusView.as_view(), name='scraping_status'),
]

