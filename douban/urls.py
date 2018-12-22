"""rest URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from douban.settings import MEDIA_ROOT
from django.views.static import serve
from books.views import BooksViewSet, CategoryViewSet
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BooksViewSet, base_name="books")
router.register(r'category', CategoryViewSet, base_name="category")

urlpatterns = [
    url('admin/', admin.site.urls),

    url('^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    #商品列表页

    url('^', include(router.urls)),

    url(r'docs/', include_docs_urls(title='firstapp')),

    url(r'^api-auth/', include('rest_framework.urls'))
]
