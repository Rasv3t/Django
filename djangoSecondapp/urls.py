from django.urls import path, include
from . import views
# student_patterns=[
#     path('list/', views.list),
#     path('groups/', views.groups),
#     path('find/<str:group_name>/', views.find),
#     path('gotostudent/<str:student_name>/', views.go_to_student)]

urlpatterns = [
    path('main/', views.index, name='index'),
    path('about/<str:name>/<int:age>/<int:course>/<str:group>/', views.about),
    path('user/', views.user),
    # path('group-info/', include(student_patterns)),
    path('homepage/', views.homepage),
    path('badrequest/', views.badrequest),
    path('forbidden/', views.forbidden),
    path('notfound/', views.notfound),
    path('servererror/', views.servererror),
    path('movie/', views.movie, name='movie'),
    path('products/', views.products, name='products'),
    path('event/', views.event, name='event'),
]