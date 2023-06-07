from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Страница выбора корпуса")

def index_m(request):
    return HttpResponse("Главная страница")