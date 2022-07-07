from django.shortcuts import render, redirect
from urllib.request import Request
from django.http import HttpResponse
from .forms import Clienteform, IngresoForm , SegForm

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def envio(request):
    return render(request,'app/envio.html')

def seguimiento(request):
    return render(request,'app/seguimiento.html')


def resultado(request):
    return render (request,'app/resultado.html')


def resumen(request):
    return render (request,'app/resumen.html')


def IngresoCliente(request):
    data= {
        'form':Clienteform()
    }
    if request.method == 'POST':
        formulario= Clienteform(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return render (request, 'app/resumen.html')
        else:
            data['form']= formulario
    return render(request, 'app/envio.html')

def IngresoEnvio(request):
    data={
        'form2':IngresoForm()
    }
    if request.method == 'POST':
        formulario=IngresoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return render (request,'app/resumen.html')
        else:
            data['form']= formulario
        return render (request,'app/envio.html')


def InfoSeguimiento(request):
    data={
        'form3':SegForm()
    }
    if request.method == 'POST':
        formulario=SegForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return render (request,'app/resultado.html')
        else:
            data['form']= formulario
        return render (request,'app/seguimiento.html')
    