from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect

def registration(request):
    browser = request.META.get('HTTP_USER_AGENT', '')
    
    if (('Mobile' in browser) or ('Symbian' in browser)
        or ('Opera M' in browser) or ('Android' in browser)
        or ('HTC_' in browser.upper()) or ('Fennec/' in browser)
        or ('Blackberry' in browser.upper()) or ('Windows Phone' in browser)
        or ('WP7' in browser) or ('WP8' in browser)):
        browser = 'Mobile'
    else:
        browser = 'Desktop'

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form, "browser":browser} )

def home(request):
    browser = request.META.get('HTTP_USER_AGENT', '')
    
    if (('Mobile' in browser) or ('Symbian' in browser)
        or ('Opera M' in browser) or ('Android' in browser)
        or ('HTC_' in browser.upper()) or ('Fennec/' in browser)
        or ('Blackberry' in browser.upper()) or ('Windows Phone' in browser)
        or ('WP7' in browser) or ('WP8' in browser)):
        browser = 'Mobile'
    else:
        browser = 'Desktop'

    return render(request, 'home.html', {'browser':browser})
