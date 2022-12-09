from django.urls import path
from . import views


app_name = 'pizzas'

urlpatterns = [
    path('',views.index, name='index'), #homepage
    path('pizzas',views.pizzas,name='pizzas'), #page with different pizzas
    path('pizza/<int:pizza_id>/',views.pizza,name='pizza'), #a selected pizza
    #path('new_pizza',views.new_pizza,name='new_pizza'),
    path('comments/pizza',views.comments,name='comments'), # the page to make comments on the pizza

]