from django.shortcuts import render,HttpResponse,redirect
from table.models import  detail

# Create your views here.
def readTable(request):
    lis=detail.objects.all()
    Col={'lis':lis}
    return render(request,'about.html',Col)


def update_place(request,pk):
    
    obj = detail.objects.get(id = pk )
    print(obj)
    
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('mail')
        salary = request.POST.get('salary')   
        lname = request.POST.get('lname')
        
        obj.firstname = name
        obj.seondname = lname
        obj.email = email
        obj.salary = salary
        obj.save()
        return redirect("about1")



    
   
    data = {"obj": obj}
    
    return render(request,'uplode.html',data)

def Create_place(request):
    
    if request.method == 'POST':
       
        name = request.POST['name']
        print(name)
        email = request.POST['email']
        print(email)
        salary = request.POST['salary']  
        print(salary)
        lname = request.POST['lname']
        print(lname)
 
        d=detail(firstname=name, seondname=lname, email=email, salary=salary)
        d.save()
        return redirect("about1")



    
    
    return render(request,'Create.html')
    
def  Delete_place(request,pk):
 
    obj = detail.objects.get(id = pk )
    print(obj)

    
    
    obj.delete()
    lis=detail.objects.all()
    Col={'lis':lis}

    return render(request,'about.html',Col)


def kyu_bhai(request):
    pass    


                                  
                                  
                                  
                                  
