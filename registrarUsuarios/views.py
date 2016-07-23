
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from .models import tb_Usuario
from django.http import Http404
from .forms import RegistrarUsuariosForm

#from django.template import loader
#import datetime

# Create your views here.
def primera_vista(request):
    #now = datetime.datetime.now()
    html = "<html><body> BIENVENIDO A PLIDCOM </body></html>"
    return HttpResponse(html)

    """obj_paises = tb_Pais.objects.all()
    #template = loader.get_template('registrarUsuarios/templates/paises.html')
    context = {'lista_paises': obj_paises}

    return render(request, 'usuarios.html', context)"""


def nuevoHabitante_registro(request):
    try:
        if request.method == 'POST':
            #si el metodo es POST se obtienen los datos del formulario
            form = RegistrarUsuariosForm(request.POST, request.FILES)

            #se comprueba si es valido el formulario
            if form.is_valid():
                 # En caso de ser valido, obtenemos los datos del formulario.
                # form.cleaned_data obtiene los datos limpios y los pone en un
                # diccionario con pares clave/valor, donde clave es el nombre del campo
                # del formulario y el valor es el valor si existe.
                cleaned_data = form.cleaned_data
                username = cleaned_data.get('username')
                email = cleaned_data.get('email')
                nombres = cleaned_data.get('nombres')
                apellidos = cleaned_data.get('apellidos')
                password = cleaned_data.get('password')
                photo = cleaned_data.get('photo')

                #instanciando un objeto para crear un usuario
                user_model = User.objects.create_user(username=username,
                password=password)
                    #email=email, nombres=nombres, apellidos=apellidos, )
                user_model.email = email
                user_model.first_name = nombres
                user_model.last_name = apellidos
                #se guarda el objeto y con ello los datos del nuevo usuario
                user_model.save()

                user_profile = tb_Usuario()
                user_profile.usr_usuario = user_model
                user_profile.usr_nombres = user_model
                user_profile.usr_apellidos = user_model
                user_profile.usr_email = user_model
                user_profile.usr_photo = photo
                user_profile.save()

                return redirect(reverse('confirmado.html',
                kwargs={'username': username}))

        else:

       # Si el mthod es GET, instanciamos un objeto RegistrarUsuariosForm vacio
            form = RegistrarUsuariosForm()
            # Creamos el contexto
            context = {'form': form}
            # Y mostramos los datos
            return render(request, 'usuarios.html', context)

    except tb_Usuario.DoesNotExist:
        imprime = " Registrate Aca!"

        raise Http404("Usuario no registrado" + imprime)

    return render(request, 'habitantes.html', {'form': form})

#Para confirmar que un usuario se registro

def confirmado(request, username):

    return render(request, 'confirmado.html', {'username': username})


def nuevo_habitante(request, user_id):
    try:
        if request.method == 'POST':
            print("yea, is POST the request")
            #reque = "is POST"
            #form = RegistrarUsuariosForm(request.POST, request.FILES)
        else:
            #form = RegistrarUsuariosForm()
            obj_user = tb_Usuario.objects.get(id_usuario=user_id)
            context = {'object': obj_user}
    except tb_Usuario.DoesNotExist:
        imprime = "OPA"

        raise Http404("Usuario no registrado" + imprime)

    return render(request, 'habitantes.html', context)