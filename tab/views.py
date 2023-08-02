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
        image = request.POST.get('image')   

        obj.pl_name = name
        obj.pl_email = email
        obj.pl_phone = phone
        obj.pl_image = image

        obj.save()

        return redirect("first1")

    data = {"obj": obj}
    
    return render(request,'upd.html',data)

def Create_place(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['mail']
        phone = request.POST['phone'] 
        image = request.FILES['image']   

        
        obj=Place(pl_name=name,pl_email=email,pl_phone=phone,pl_image=image)

        obj.save()

        return redirect("first1")

  
    
    return render(request,'retab.html')


def Delete_place(request,pk):
    obj = Place.objects.get(id = pk)
    obj.delete()


  
    show = Place.objects.all()
    data = {"show": show}

    return render(request,'index.html',data)


def view(request,pk):
    show = Place.objects.get(id=pk)
    data = {"show": show}
    return render(request,'view.html',data)

    # return render(request,'index.html',data)
    # obj = Place.objects.get(id = pk )
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('mail')
    #     phone = request.POST.get('phone')   
    #     image = request.POST.get('image')   

    #     obj.pl_name = name
    #     obj.pl_email = email
    #     obj.pl_phone = phone
    #     obj.pl_image = image

    #     obj.save()

    #     return redirect("first1")
    
    # # show = Place.objects.all()
    # data = {"obj": obj}
    # return render(request,'view.html',data)


    
   






# def EmployeeTable(request):
#     data= Employee.objects.all()
#     div={"data":data}
#     return render(request,'about.html',div)


# # Create your views here.
# def first(request):
#     return render(request,'index.html')
