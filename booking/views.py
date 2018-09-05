from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from .models import Book, Bank


def index(request):
    return render(request, 'booking/index.html')


def detail(request):
    source = request.GET['p']
    destination = request.GET['q']
    date = request.GET['r']
    passengers = request.GET['s']
    try:
        is_return = request.GET['i']
    except:
        is_return = 'No'

    trains = get_list_or_404(Book, Source=source, Destination=destination, Date=date)

    return render(request, 'booking/detail.html', {'trains': trains, 'passengers': passengers, 'is_return': is_return})


def book(request, amt, passengers, is_return):
    return render(request, 'booking/book.html', {'amt': amt, 'passengers': passengers, 'is_return': is_return})


def status(request):
    card_number = request.GET['p']
    card_holder = request.GET['q']
    expiry = request.GET['r']
    cvv = request.GET['s']

    try:
        details = Bank.objects.get(Card_Holder=card_holder)
    except Bank.DoesNotExist:
        return HttpResponse('<h3>Payment Failed</h3>')

    if details.Card_Number == card_number and details.Expiry == expiry and details.CVV == cvv:
        return HttpResponse('<h3>Payment Successful</h3>')
    else:
        return HttpResponse('<h3>Payment Failed</h3>')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'booking/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'booking/index.html')
            else:
                return render(request, 'booking/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'booking/login.html', {'error_message': 'Invalid login'})
    return render(request, 'booking/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'booking/index.html')
    context = {
        "form": form,
    }
    return render(request, 'booking/register.html', context)
