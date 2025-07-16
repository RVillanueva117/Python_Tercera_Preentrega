from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from django.template import loader
from AppCoder.form import Curso_formulario
from AppCoder.models import Alumno
from .models import Profesor
from AppCoder.form import Alumno as alumno_formulario
from AppCoder.form import Profesor as profesor_formulario
from AppCoder.models import Profesor
Profesor.objects.all()


def inicio(request):
    return render(request, "padre.html")

def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template('cursos.html')
    documento = plantilla.render(dicc)
    return HttpResponse(documento)
    

def alta_curso(request, nombre):
    curso = Curso(nombre=nombre, camada=99999)
    curso.save()
    msj = f"se guardó el curso {curso.nombre} {curso.camada}"
    return HttpResponse(msj)


def buscar_curso(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        if nombre:
            cursos = Curso.objects.filter(nombre__icontains=nombre)
            if cursos.exists():
                return render(request, "resultado_busqueda_curso.html", {"cursos": cursos})
            else:
                return HttpResponse("No se encontraron cursos con ese nombre.")
    return render(request, "buscar_curso.html")


def profesores(request):
    return render (request, "profesores.html")

def buscar_profesor(request):
    if request.method == "POST":
        apellido = request.POST.get("apellido")
        if apellido:
            profesores = Profesor.objects.filter(apellido__icontains=apellido)
            return render(request, "resultado_busqueda_profesor.html", {"profesores": profesores})
        else:
            return HttpResponse("Por favor, ingrese un apellido para buscar.")
    
    return render(request, "buscar_profesor.html")

def alta_profesor(request):
    if request.method == "POST":
        formulario = profesor_formulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            profesor = Profesor(**data)
            profesor.save()
            return HttpResponse("Profesor creado exitosamente")
    else:
        formulario = profesor_formulario()

    return render(request, "alta_profesor.html", {"formulario": formulario})

def lista_profesor(request):
    profesores = Profesor.objects.all()
    return render(request, "lista_profesor.html", {"profesores": profesores})

def alumnos(request):
    print(">>> Vista alumnos ejecutada <<<") 
    alumnos = Alumno.objects.all()
    return render(request, "alumnos.html", {"alumnos": alumnos})

def buscar_alumno(request):
    if request.method == "POST":
        documento = request.POST.get("documento")

        if documento:
            try:
                alumno = Alumno.objects.get(documento=documento)
                return render(request, "resultado_busqueda_alumno.html", {"alumno": alumno})
            except Alumno.DoesNotExist:
                return render(request, "resultado_busqueda_alumno.html", {
                    "alumno": None,
                    "documento": documento
                })
        else:
            return render(request, "buscar_alumno.html", {
                "error": "Ingresar un documento para buscar."
            })

    return render(request, "buscar_alumno.html")


def alta_alumno(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        documento = request.POST.get("documento")
        fecha_nacimiento = request.POST.get("fecha_nacimiento")
        email = request.POST.get("email")
        edad = request.POST.get("edad")

        alumno = Alumno(
            nombre=nombre,
            apellido=apellido,
            documento=documento,
            fecha_nacimiento=fecha_nacimiento,
            email=email,
            edad=edad
        )
        alumno.save()
   

    return render(request, "alta_alumno.html")



def contacto(request):
    return render (request, "contacto.html")


def curso_formulario(request):
   
   if request.method == "POST":
        mi_formulario=Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data  
            curso = Curso(nombre=datos['nombre'], camada=datos['camada'])
            curso.save()
            return HttpResponse(f"Curso {curso.nombre} creado con éxito.")
        
   
   return render(request, "curso_formulario.html")



def buscar(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        if nombre:
            cursos = Curso.objects.filter(nombre__icontains=nombre)
            return render(request, "resultado_busqueda.html", {"cursos": cursos})
        else:
            return HttpResponse("Debes ingresar un nombre para buscar.")