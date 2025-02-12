from django.shortcuts import*
from all_students.models import*
from all_students.forms import*

# Create your views here.
def home(request):
  return render(request,'home.html')

# reade opretions
def all_students(request):
  data = Student_registration.objects.all()
  context = {'data':data}
  return render(request,'all_students.html',context)

# create opretions
def stu_reg(request):
  if request.method=="POST":
    
    form =Stu_reg_forms(request.POST,request.FILES)
    try:
      if form.is_valid():
        form.save()
        return redirect('all_students')
    except Exception as e:
        return HttpResponse("Somthing went rong!",e)
  else:    
    form = Stu_reg_forms()

  context = {'form':form}
  print(form)
  return render(request,'stu_reg.html',context)


# dekete opretins
def delete_stu(request,id):
  try:
    data = Student_registration.objects.get(pk=id)
    if request.method == "POST":
      data.delete()
      return redirect("all_students")
    else:
      return HttpResponse("Nothing to delete")
  except Exception as e:
    return HttpResponse(e,"Opps 404 page not found")
  
def stu_details(request,id):
  data=Student_registration.objects.filter(id=id)
  all_data = Student_registration.objects.all()
  context={'data':data,'all_data':all_data}
  return render(request,'stu_details.html',context)

  
  
  
#update opretins

def update_student(request,id):
  data = Student_registration.objects.get(pk=id)
  if request.method=="POST":
      form =Stu_reg_forms(request.POST,instance=data)
      form.save()
      return redirect('all_students')
  else:
      form=Stu_reg_forms(instance=data)
      print()
      return render(request,'update_student.html',{'form':form})
    
  
   

   