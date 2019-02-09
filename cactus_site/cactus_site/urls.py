"""cactus_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from main.views import (main, news, about, attributes,
                        books, catalogue, club_member, passage,
                        count_member)

urlpatterns = [
    path('', main),
    path('admin/', admin.site.urls),
    path('news/', news),
	path('about/', about),
    path('attributes/', attributes),
    path('books/', books),
    path('catalogue/', catalogue),
    path('club_member/', club_member),
    path('passage/', passage),
    path('club_member/1', count_member)
]
