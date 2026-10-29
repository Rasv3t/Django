from django.urls import path
from .views import homepageview, about, hobby, city, contacts

urlpatterns = [path('', homepageview, name='home'),
               path('about/', about, name='MyAbout'),
               path('hobby/', hobby, name='MyHobby'),
               path('city/', city, name='MyCity'),
               path('contacts/', contacts, name='MyContacts'),]
