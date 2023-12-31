from django.shortcuts import render
from basic_api.forms import Employee_form_create,Employee_form_delete,Employee_form_read,Employee_form_update
from basic_api.models import Employee_data
# Create your views here.


def index(request):
    return render(request,'basic_api/index.html')

def read(request):
    Flag=False
    Flag2=False
    content={'Form':Employee_form_read(),'Flag':Flag,'Flag2':Flag2,'emp_name_read':'','emp_id_read':'','message':''}
    if(request.method=="GET"):   
        emp_read=Employee_form_read(request.GET)
        if ('emp_id' in request.GET):
            emp_id=int(request.GET['emp_id'])
            try:
                emp_data=Employee_data.objects.get(emp_id=emp_id)
                emp_name_read=emp_data.name
                emp_id_read=emp_data.emp_id
                message='Succesfully Found'
                Flag2=False
                content['emp_name_read']=emp_name_read
                content['emp_id_read']=emp_id_read
                content['message']=message
                content['Flag2']=Flag2
                content['Flag']=Flag

            except:
                content['Flag2']=True
                
                content['message']='NOT Found'
                return render(request,'basic_api/read.html' ,context=content)
            
        else:
            content['message']='NOT Found'
            return render(request,'basic_api/read.html' ,context=content)
    else:
        content['message']='NOT Found'
        return render(request,'basic_api/read.html' ,context=content)
    return render(request,'basic_api/read.html',context=content)


def write(request):

    Flag=False
    message=''
    
    if(request.method=="POST"):
        
        emp_write=Employee_form_create(request.POST)
        if (emp_write.is_valid()): 
            name=request.POST.get('name')
            emp_id=int(request.POST.get('emp_id'))
            try:
                new_emp_data=Employee_data(name=name,emp_id=emp_id)
                new_emp_data.save()
                Flag=True
                message=' Succesfully Updated Employee Data'
                print('-------write try----------')
            except:
                print('------except partwrite------')
                message='Employee ID already Present' 
    
        else:    
            message=' NOT Succesfull'
    else:
         message=''
    return render(request,'basic_api/write.html',{'Form':Employee_form_create(),'message':message, 'Flag':Flag})


def update(request):
    return render(request,'basic_api/update.html')

def delete(request):
    return render(request,'basic_api/delete.html')



