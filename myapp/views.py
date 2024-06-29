from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.models import Food
from myapp.forms import FoodForm

# Create your views here.

class FormCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=FoodForm()

        return render(request,"food_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
         
         form_instance=FoodForm(request.POST)

         if form_instance.is_valid():
              
              data=form_instance.cleaned_data

              Food.objects.create(**data)
              
              return  redirect("food-list")
         else:
              return render(request,"food_add.html",{"form":form_instance})
       

class FormListView(View):

        def get(self,request,*args,**kwargs):
             
             qs=Food.objects.all()

             return render(request,"food_list.html",{"data":qs})
        


