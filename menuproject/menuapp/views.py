from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

# Create your views here.

def addFoodView(request):
    form = ItemForm
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'menuapp/add_food.html'
    context = {'form': form}
    return render(request, template_name, context)

def showFoodView(request):
    obj = Item.objects.all()
    template_name = 'menuapp/show_menu.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def detailedFoodView(request, f_id):
    obj = Item.objects.get(id=f_id)
    template_name = 'menuapp/food_details.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def updateFoodView(request, f_id):
    obj = Item.objects.get(id=f_id)
    form = ItemForm(instance=obj)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'menuapp/add_food.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteFoodView(request, f_id):
    obj = Item.objects.get(id=f_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('show')
    template_name = 'menuapp/delete_food.html'
    context = {'obj': obj}
    return render(request, template_name, context)
