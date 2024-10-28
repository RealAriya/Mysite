from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from website.views import http_test,json_test    #To currect directory we use .views or directory-name(mysite).views
# change directory in your app (website)

# path ('url address' , 'view')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls', namespace='website')),
    path('blog/',include('blog.urls', namespace='blog'))    # we can remove 'website/' to have a real site
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
