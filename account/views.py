from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form": form
        }
        return render(request, "registration/signup.html", context)
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to="aggregrator:search")
        return HttpResponseBadRequest("Inputs are not valid")
    else:
        return HttpResponseNotAllowed()

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) #request.POST is not the first expected parameter
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if ('next' in request.POST):
                return redirect(request.POST.get('next'))
            return redirect(to="aggregrator:search")        
    else: 
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect(to="account:login")