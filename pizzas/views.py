from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'pizzas/index.html')



def pizzas(request):
    pizzas = Pizza.objects.order_by()

    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html', context)

def pizza(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = Topping.objects.filter(pizza=pizza)
    comments = Comment.objects.filter(pizza=pizza)

    context = {'pizza':pizza, 'toppings':toppings}

    return render(request, 'pizzas/pizza.html',context)

'''
def new_pizza(request):
    if request.method != 'POST':
        form = PizzaForm()
    else:
        print(request.POST)
        form = PizzaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:pizzas')

    context = {'form':form}
    return render(request, 'pizzas/new_pizza.html',context)
'''

'''
def new_topping(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = ToppingForm()
    else:
        print(request.POST)
        form = ToppingForm(data=request.POST)
        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            new_topping.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)

    context = {'form':form,'pizza':pizza}
    return render(request, 'pizzas/new_topping.html',context)
    '''

def comments(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentsForm()
    else:
        print(request.POST)
        form = CommentsForm(data=request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.pizza = pizza
            comments.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)

    context = {'form':form,'pizza':pizza}
    return render(request, 'pizzas/comments.html',context)






