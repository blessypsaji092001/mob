"""mobiles URL Configuration

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
from django.urls import path

from django.contrib import admin
from django.urls import path
from greetings import views
from calculator import views as cview
from blogapi import views as bview
from mobile.views import MobilesView,MobileDetailView
from cloth.views import ClothsView,ClothDetailView
from mobapi import views as apiview
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/teq/mobiles",apiview.MobileView.as_view()),
    path("api/v1/teq/mobiles/<int:id>",apiview.MobileDetailView.as_view()),
    path("api/v2/teq/mobiles",apiview.MobileModelView.as_view()),
    path("api/v2/teq/mobiles/<int:id>",apiview.MobileModelView.as_view())
    # path('goodmorning/',views.GoodMorningView.as_view()),
    # path("operations/add/",cview.AddView.as_view()),
    # path("operations/sub/",cview.subView.as_view()),
    # path("operations/mul/", cview.mulView.as_view()),
    # path("operations/fac/", cview.facView.as_view()),
    # path("operations/wordcount",cview.WordCountView.as_view()),
    # path("social/post/",bview.PostsView.as_view()),
    # path("social/posts/<int:pid>",bview.PostDetailsView.as_view()),
    # path("api/v1/mobiles",MobilesView.as_view()),
    # path("api/v1/mobiles/<int:id>",MobileDetailView.as_view()),
    # path("api/cloth/",ClothsView.as_view()),
    # path("api/cloth/<int:id>",ClothDetailView.as_view())
]
