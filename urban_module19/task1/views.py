from django.shortcuts import render
from task1.forms import UserRegister
from task1.models import *
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    return render(request, 'first_task/index.html')


def games(request):
    games = list(Game.objects.all())
    context = {
        "games": games
    }
    return render(request, 'first_task/games.html', context)


def cart(request):
    return render(request, 'first_task/cart.html')

def news(request):
    news_ = News.objects.all().order_by('date')
    paginator = Paginator(news_, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'first_task/news.html', {'news': page_obj})


info = {}

def sign_up_by_django(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            info["error"] = get_error(username, password, repeat_password, age)
            if info["error"] == "":
                Buyer.objects.create(name=username, balance=0, age=age)
                info["result"] = f"Приветствуем, {username}!"
            else:
                info["result"] = ""
    else:
            form = UserRegister()
    info["form"] = form
    return render(request,'first_task/registration_page.html', info)


def get_error(username: str, password: str, repeat_password: str, age: int):
    users = list(Buyer.objects.values_list('name', flat=True))

    if username.lower() in [x.lower() for x in users]:
        return "Пользователь уже существует"
    if password != repeat_password:
        return "Пароли не совпадают"
    if int(age) < 18:
        return "Вы должны быть старше 18"
    return ""