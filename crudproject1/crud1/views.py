from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from crud1.models import Recipe

# Create your views here.
def index(request):
	return render(request,'index.html')

def display(request):
	if request.method == "POST":
		name=request.POST.get('name')
		ingredients=request.POST.get('ingredients')
		instructions=request.POST.get('instructions')
		image=request.FILES.get('image')
		

		recipe=Recipe(name=name,ingredients=ingredients,instructions=instructions,image=image)
		recipe.save()

		return render(request,'index.html')

def read(request):
	data=Recipe.objects.all()
	return render(request,'read.html',{'data':data})

def update(request):
	return render(request,'update.html')

def update_data(request):
	name=request.POST.get('name')
	recipe=get_object_or_404(Recipe,name=name)
	if request.method == "POST":
		new_ingredients=request.POST.get('ingredients')
		new_instruction=request.POST.get('instructions')
		new_image=request.FILES.get('image')

		recipe.ingredients=new_ingredients
		recipe.instructions=new_instruction
		recipe.image=new_image
		recipe.save()

		return render(request,'update.html')

def delete(request):
	return render(request,'delete.html')


def delete_data(request):
	name=request.POST.get('name')
	recipe=get_object_or_404(Recipe,name=name)
	if request.method == "POST":
		recipe.delete()

	return render(request,'delete.html')

"""
def delete_data(request):
	if request.method == "POST":
		name=request.POST.get('name')
		data=Recipe.objects.filter(name=name)
		data.delete()

		return render(request,'delete.html')
"""