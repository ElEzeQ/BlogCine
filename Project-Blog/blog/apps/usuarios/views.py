from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
from .forms import FormularioRegistro
from django.contrib import messages


def registro(request):
    contexto={}

    if request.method == "POST":
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            nombre_usuario = formulario.cleaned_data["username"]
            messages.success(request, f"Usuario {nombre_usuario} creado.")
            return redirect(reverse("posts:Inicio"))
    else:
        formulario = FormularioRegistro()

    contexto["form"] = formulario
    return render(request, "usuarios/register.html", contexto)
