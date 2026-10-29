from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError

def product_list(request):
    # header = 'Данные пользователя'
    # langs = ['Python', 'Java', 'C++']
    # user = {'name': 'Tom', 'age': 18}
    # address = ('Апельсин', 23, 45)
    # data = {'age': 70}
    products = [
        {'name': 'Ноутбук', 'price': 55000},
        {'name': 'Смартфон', 'price': 30000},
        {'name': 'Планшет', 'price': 20000},
    ]
    return render(request, 'index.html', {'products': products})

def about(request, name, age, course, group):
    return HttpResponse(f'''
        <h2>Основная информация обо мне:</h2>
        <h3>Имя - {name}
        <p>Возраст - {age}</p>
        <p>Курс - {course}</p>
        <p>Группа - {group}</p>
        </h3>
        ''')

def user(request):
    name = request.GET.get('name', 'Не указано')
    age = request.GET.get('age', 'Не указано')
    course = request.GET.get('course', 'Не указано')
    group = request.GET.get('group', 'Не указано')
    return HttpResponse(f'<h2>Имя: {name} <p>Возраст: {age}</p><p>Курс: {course}</p><p>Группа: {group}</p></h2>')

STUDENTS = {
        'ИСт-241': ['Агаповка', 'Шмидт', 'Щербаков'],
        'ИСт-242': ['Дудка', 'И Трубник', 'Гай Юлий Цезарь'],
        'ИСт-243': ['Морзаков', 'Пупков', 'Фандеева'],
    }

def list(request):
    html = ''
    for group, students in STUDENTS.items():
        items = ''.join(
            f'<a href="http://127.0.0.1:5681/group-info/gotostudent/{s}"><li>{s}</li></a>'
            for s in students
        )
        html += f'''
        <h2><a href="http://127.0.0.1:5681/group-info/find/{group}">{group}</a></h2>
        <ul>{items}</ul>
        '''
    return HttpResponse(html)

def groups(request):
    li = ''.join(f'<h1><li><a href="http://127.0.0.1:5681/group-info/find/{item}">{item}</a></li></h1>' for item in STUDENTS)
    html = f'''
    <ul>{li}</ul>
    <p><h3>Групп в списке: {len(STUDENTS)}</h3></p>
    '''
    return HttpResponse(html)

def find(request, group_name):

    students = STUDENTS.get(group_name, [])
    items = ''.join(f'<a href="http://127.0.0.1:5681/group-info/gotostudent/{s}"><li>{s}</li></a>' for s in students)
    return HttpResponse(f'''
    <h2>{group_name}</h2>
    <h3><ul>{items}</ul></h3>
    ''')

def go_to_student(request, student_name):
    return HttpResponse(f'''
    <h2>Студент {student_name}</h2>
    ''')

def homepage(request):
    return HttpResponsePermanentRedirect('/')

def badrequest(request):
    return HttpResponseBadRequest()

def forbidden(request):
    return HttpResponseForbidden()

def notfound(request):
    return HttpResponseNotFound()

def servererror(request):
    return HttpResponseServerError()

general_info = {
    'title': 'KIRILL CORPORATION'
}

def index(request):
    variad = {
        'description': 'Этот сайт сделан на коленке душевно больным человеком',
        'user_name': 'Сашенька',
        'user_age': 18,
        'city': 'Полыс-Анжелес',
    }
    context = {**general_info, **variad}
    return render(request, 'index.html', context)

def movie(request):
    movie_data = {
        'name': 'ОППЕНГЕЙМЕР',
        'year': 2023,
        'director': 'Кристофер Нолан',
        'metascore': 90,
        'IMDb_rating': 8.2,
    }
    context = {**general_info, **movie_data}
    return render(request, 'movie.html', context)

def products(request):
    tovari = [
        {'name': 'Ноутбук', 'category': 'Электроника', 'price': 77999, 'stock': True},
        {'name': 'Стиральная машинка', 'category': 'Электроника', 'price': 34890, 'stock': True},
        {'name': 'Миксер', 'category': 'Электроника', 'price': 9990, 'stock': False},
        {'name': 'Куртка кожаная', 'category': 'Одежда', 'price': 27590, 'stock': True},
        {'name': 'Браслет позолоченный', 'category': 'Ювелирные украшения', 'price': 29999, 'stock': False},
        {'name': 'Клавиатура', 'category': 'Электроника', 'price': 4890, 'stock': False},
    ]
    context = {**general_info, 'tovari': tovari}
    return render(request,'products.html', context)

def event(request):
    return render()