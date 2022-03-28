from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate

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