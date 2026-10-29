from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return HttpResponse('<h1>Привет!</h1> <p>Я <b>Фролов Кирилл Михайлович,</b> и я обучаюсь в группе <b>ИСт-243</b></p> <p><a href="http://127.0.0.1:5681/about/">about</a> <a href="http://127.0.0.1:5681/hobby/">hobby</a> <a href="http://127.0.0.1:5681/city/">city</a> <a href="http://127.0.0.1:5681/contacts/">contacts</a></p>')

def about(request):
    return HttpResponse('<h1>Обо мне:</h1> <p>Я изучаю django и люблю программировать!</p> <p><a href="http://127.0.0.1:5681/">На главную</a></p>')

def hobby(request):
    return HttpResponse('<h1>Мои хобби:</h1> <p>Изучение ЯП и видеоигры</p> <p><a href="http://127.0.0.1:5681/">На главную</a></p>')

def city(request):
    return HttpResponse('<h1>Город:</h1> <p>Я проживаю в городе Кемерово</p> <p><a href="http://127.0.0.1:5681/">На главную</a></p>')

def contacts(request):
    return HttpResponse('<h1>Мои контакты:</h1> <p> Email - kifrokirfro@gmail.com</p> <p><a href="http://127.0.0.1:5681/">На главную</a></p>')