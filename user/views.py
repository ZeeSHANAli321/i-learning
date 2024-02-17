from django.shortcuts import render,HttpResponse,redirect
from .models import contact,batch,signUpModel

# Create your views here.
def index(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        sub=request.POST.get('sub')
        msg=request.POST.get('msg')
        contact(fname=fname,lname=lname,email=email,sub=sub,msg=msg).save()
        return HttpResponse('<script> alert("Thanks For Contacting Us , We will connect to you as soon as possible . "); location.href="" ; </script>')


    return render(request,'user/index.html')

def base(request):
    return render(request,'user/base.html')

def signUp(request):
    Bs=batch.objects.all()
    Context={
        'Bs':Bs,
    }

    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        pswrd=request.POST.get('pass')
        choosedBatch=request.POST.get('choosedBatch')
        image=request.FILES.get('image')

        isEmail = signUpModel.objects.filter(email=email).exists()
        isPhone = signUpModel.objects.filter(phone=phone).exists()

        if isEmail:
            return HttpResponse('<script>alert("The provided Email is already is Registered "); location.href="/signUp/";</script>')

        elif isPhone:
            return HttpResponse('<script>alert("The provided Phone No is already is Registered"); location.href="/signUp/";</script>')
        else :
            newSt=signUpModel(fname=fname,lname=lname,email=email,phone=phone,pswrd=pswrd,image=image)
            newSt.save()
            selected_batch = batch.objects.get(id=choosedBatch)
            newSt.sBatch.set([selected_batch])

            return HttpResponse('<script>alert("You are Signed Up succesfully Now Login To proceed Further."); location.href="/login/";</script>')


    else:
        return render(request,'user/signUp.html',Context)


def logIn(request):
    if request.method=='POST':

        email=request.POST.get('email')
        pswrd=request.POST.get('pswrd')

        
        isStudent = signUpModel.objects.filter(email=email,pswrd=pswrd).exists()

        if isStudent:
                request.session['sId']=email
                return redirect('/student/dashboard')
        else :
                return HttpResponse('<script>alert("invalid id password "); location.href="/login/";</script>')


    return render(request,'user/login.html')

def resetPass(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        newPss=request.POST.get('newPass')
        

        
        isValid = signUpModel.objects.filter(fname=fname,lname=lname,email=email,phone=phone).exists()
        if isValid:
             
             user=signUpModel.objects.get(email=email)
             user.pswrd=newPss
             user.save()
             
             

             
             return HttpResponse('<script>alert("Password reset succesfully "); location.href="/login/";</script>')

        else:
             return HttpResponse('<script>alert("Data does not match "); location.href="/resetPass/";</script>')            
        
       
             


    else :
          return render(request,'user/resetPass.html')



    

    

        

        
    
    

