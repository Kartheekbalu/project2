from django.contrib import admin
from django.urls import path
from example1.views import Home,blog,update,uprec,delete ,search
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='Home'),
    path('blog',blog,name='blog'),
    path('base.html',Home,name='Home'),
    path('update/<int:id>/',update,name='update'),
    path('update/uprec/<int:id>/',uprec,name='uprec'),
    path('delete/<int:id>/',delete,name='delete'),
    path('search',search, name="search"),
]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)