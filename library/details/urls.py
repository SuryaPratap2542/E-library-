from django.urls import path
from details import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("",views.Login,name="login"),
    path("home",views.Home,name="home")
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
