from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.inicio, name="inicio"),
   
   
    path("buscar_profesor", views.buscar_profesor, name="buscar_profesor"),
    path("alta_profesor", views.alta_profesor, name="alta_profesor"),
        path("alumnos/", views.alumnos, name="alumnos"),
    path("buscar_alumno", views.buscar_alumno, name="buscar_alumno"),
    path("alta_alumno", views.alta_alumno, name="alta_alumno"),
    path("cursos", views.cursos, name="cursos"),
    path("contacto", views.contacto, name="contacto"),
     #path('alta_curso/<nombre>', views.alta_curso),
    path("alta_curso", views.curso_formulario, name="alta_curso"),
    path('buscar_curso/', views.buscar_curso, name="buscar_curso"),
    path("buscar", views.buscar),
    path("profesores/", views.lista_profesor, name="profesores"),
    ]


