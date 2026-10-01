from django.urls import path
from . import views # 5 agregamos nuestro aca vamos a integrar nuestro pat

app_name = 'inicio' #|8 agregamos nuestro app_name 
#|9 agregamos nuestra ruta para que nos lleve a nuestro html
urlpatterns = [
    path('', views.index, name='index'), #4 aca temos nuestra ruta

]