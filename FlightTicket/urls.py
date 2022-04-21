"""FlightTicket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from booksystem import views
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^booksystem/admin/', admin.site.urls),
    url(r'^booksystem/admin/finance', views.admin_finance, name='admin_finance'),  # 财务管理
    url(r'^booksystem/', include('booksystem.urls')),
    url(r'', include('booksystem.urls')),
]
