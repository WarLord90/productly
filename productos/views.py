# from django.http import HttpResponse, JsonResponse -- en caso de salir a prod o como prototipo de manera rápida
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import ProductoForm
from .models import Producto
# Create your views here.

# en caso de salir a prod o como prototipo de manera rápida
# def index(request):
#     # tipos de consulta a la base de datos
#     # productos = Producto.objects.all()
#     # productos = Producto.objects.filter(puntaje=3)
#     # productos = Producto.objects.get(id=1)
#     productos = Producto.objects.all().values()
#     # print(productos)
#     return JsonResponse(list(productos), safe=False)


def index(request):
    productos = Producto.objects.all()

    return render(
        request,
        'index.html',
        context={'productos': productos}
    )


def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(
        request,
        'detalle.html',
        context={'producto': producto}
    )


def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductoForm()

    return render(
        request,
        'producto_form.html',
        {'form': form}
    )
