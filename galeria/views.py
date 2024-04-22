from django.shortcuts import render , get_object_or_404, redirect
from galeria.models import Fotografia
from django.contrib import messages

# Create your views here.
def index(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada = True)
    # .order_by() define a ordem com que os objetos serão trazidos e .filter() define quais objetos serão trazidos à partir de um filtro
    if not request.user.is_authenticated: #se o usuário n ta logado ele n consegue ir pro index
        messages.error(request,"Usuário não logado.")
        return redirect('login')
    
    return render(request,'galeria/index.html',{"cards":fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk= foto_id)
    return render(request,'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request,):
    if not request.user.is_authenticated: #se o usuário n ta logado ele n consegue ir pro index
        messages.error(request,"Usuário não logado.")
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada = True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html",{"cards":fotografias})