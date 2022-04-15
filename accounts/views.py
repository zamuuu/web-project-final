from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from .models import UserExtension
from .forms import NuestroUserForm, NuestroEditForm
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
    
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                return render(request, 'accounts/login.html', {'login_form': login_form, 'msg': 'No te has podido autenticar, primero debes registrarte'})
        else:
                return render(request, 'accounts/login.html', {'login_form': login_form, 'msg': 'El formulario ingresado no es valido, porfavor vuelve a intentarlo'})
    login_form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'login_form': login_form})


def logout(request):
    ...


def register(request):
    
    if request.method == 'POST':
        form = NuestroUserForm(request.POST)
    
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'index/index.html', {'msj': f'Se creo el usuario {username} CORRECTAMENTE ✓'})
        else:
            return render(request, 'accounts/register.html', {'form': form})

    form = NuestroUserForm()    
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def edit(request):
    
    logged_user,_ = UserExtension.objects.get_or_create(user=request.user)
    
    msj = ''
    
    if request.method == 'POST':
        form = NuestroEditForm(request.POST, request.FILES)
    
        if form.is_valid():
            data = form.cleaned_data
            
            request.user.email = data.get('email',)
            request.user.first_name = data.get('first_name', '')
            request.user.last_name = data.get('last_name', '')
            if data.get('password1') == data.get('password2') and len(data.get('password1')) > 8:
                request.user.set_password(data.get('password1'))

            logged_user.more_description = data.get('more_description', '')
            avatar = data.get('avatar', '')
            if avatar is not None:
                if avatar is False:
                    logged_user.avatar = None
                else:
                    logged_user.avatar = data.get('avatar')

            request.user.save()
            logged_user.save()
            
            msj = 'Se ha modificado tu usaurio correctamente'
            return render(request, 'index/index.html', {'msj': msj})
        else:
            return render(request, 'accounts/editar_user.html', {'form': form})
        
    form = NuestroEditForm(
        initial={
            'username': request.user.username,
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'password1': '',
            'password2': '',
            'avatar': logged_user.avatar,
            'more_description': logged_user.more_description
        }
    )
    return render(request, 'accounts/editar_user.html', {'form': form})

def detail(request):
    return render(request, 'accounts/detail_user.html', {})