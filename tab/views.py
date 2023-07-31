from django.shortcuts import render,redirect
from tab.models import Place

# Create your views here.
def  PlaceTable(request):
    show = Place.objects.all()
    data = {"show": show}

    return render(request,'index.html',data)

def update_place(request,pk):
    obj = Place.objects.get(id = pk )
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('mail')
        phone = request.POST.get('phone')   
        obj.pl_name = name
        obj.pl_email = email
        obj.pl_phone = phone
        obj.save()

        return rediret("first")

    data = {"obj": obj}
    
    return render(request,'upd.html',data)


    
   






# def EmployeeTable(request):
#     data= Employee.objects.all()
#     div={"data":data}
#     return render(request,'about.html',div)


# # Create your views here.
# def first(request):
#     return render(request,'index.html')
