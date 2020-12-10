from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.contrib import auth
from django.urls import reverse

def login(request):
    title = 'вход'

    login_form = ShopUserLoginForm(data=request.POST or None)
    next_url = request.GET.get('next', '')
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            return HttpResponseRedirect(reverse('main'))

    content = {'title': title, 'login_form': login_form, 'next': next_url}
    return render(request, 'authapp/login.html', content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        register_form = ShopUserRegisterForm()

    content = {'register_form': register_form}
    return render(request, 'authapp/register.html', content)


def edit(request):
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('authapp/edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {'register_form': edit_form}
    return render(request, 'authapp/edit.html', content)


