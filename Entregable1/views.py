from django.http import HttpResponse
from django.template import Template, Context 
from django.template import loader
from EntregableApp.models import Familiares 

def first_template(self):
    familiar = Familiares(nombre="Karina", apellido="Surt", fechaDeNacimiento = "1986-8-4", edad = 35 )
    familiar.save()
    diccionario = {"familiar":familiar}
    
    familiar1 = Familiares(nombre="ALejandro", apellido="SUrt00", fechaDeNacimiento = "1978-11-26", edad = 44 )
    familiar1.save()
    diccionario["familiar1"] = familiar1
    
    familiar2 = Familiares(nombre="Carlos", apellido="Silva", fechaDeNacimiento = "1955-11-15", edad = 66 )
    familiar2.save()
    diccionario["familiar2"] = familiar2
    
    plantilla = loader.get_template("template02.html")
    documento = plantilla.render(diccionario)
    """documento = f"Curso:{curso.nombre} - Camada: {curso.camada}"""
    return HttpResponse(documento)

