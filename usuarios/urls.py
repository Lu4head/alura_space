from django.urls import path
from usuarios.views import login, cadastro
#from usuarios.views import 

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro')
]