from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from appStore.views.login.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginFormView.as_view()),
    path('store/', include('appStore.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)