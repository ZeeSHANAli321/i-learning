from django.shortcuts import render,HttpResponse,redirect
from user.models import *
from alpha import ChatBot
from student.models import sbmtAssignment,thoughts,complaint,chat,chatBase


# Create your views here.

def isSession(request):
    if request.session.has_key('sId'):
        isValid=signUpModel.objects.filter(email=request.session['sId'])
        if isValid.exists:
            st=signUpModel.objects.get(email=request.session['sId'])
            return st
    else:
        return None
    
def stDashboard(request):
    st=isSession(request)
    if st!=None:
        return render(request,'student/base.html',{'st':st})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">404 Not-found</h1></body>')
     
def dashboard(request):
    st=isSession(request)
    if st!=None:
        thought = thoughts.objects.order_by('?').first()
        return render(request,'student/dashboard.html',{'st':st,'th':thought})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">404 Not-found</h1></body>')
       
def videoLectures(request):
    st=isSession(request)
    if st!=None:
        return render(request,'student/video.html',{'st':st})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">404 Not-found</h1></body>')

def playVideo(request,vId,bId):
    st=isSession(request)
    if st!=None:
        pVideo=video.objects.get(id=vId)
        pBatch=batch.objects.get(id=bId)
        return render(request,'student/playVideo.html',{'st':st,'pv':pVideo,'pb':pBatch})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">404 Not-found</h1></body>')

def eNotes(request):
    st=isSession(request)
    if st!=None:
        return render(request,'student/eNotes.html',{'st':st})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">404 Not-found</h1></body>')
       
def assignments(request):
    st=isSession(request)
    if st!=None:
        if request.method=='POST':
            fname = st.fname  
            bname = request.POST.get('bname') 
            assignmentId=request.POST.get('assignmentId')
            aid=f"{assignmentId}_{bname}"
            name = bname
            date=timezone.now()
            file = request.FILES.get('aFile')
           
            def isSubmitted(self):
                if st.submittedAssignment.filter(name=assignments.name).exists():
                    return True
                else :
                    return False
            
           
            if file:
                 anew=sbmtAssignment(assignmentId=assignmentId,name=name,date=date,file=file)
                 anew.save()
                 st.submittedAssignment.add(anew)
            else :
                HttpResponse('hello ')
        return render(request,'student/assignment.html',{'st':st})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">404 Not-found</h1></body>')
     
def studyMaterials(request):
    st=isSession(request)
    if st!=None:
        sM=sMaterial.objects.all()
        return render(request,'student/studymaterial.html',{'st':st,'sM':sM})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">404 Not-found</h1></body>')

def timings(request):
    st=isSession(request)
    if st!=None:
       
        return render(request,'student/timings.html',{'st':st})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">404 Not-found</h1></body>')

#Doubts ai view 
""" def doubts(request):
    st=isSession(request)
    if st!=None:
        #To show list of all chatbase in reverse order
        reveCB = st.pchats.all().order_by('-id')
        #ChatBot instance
        alpha = ChatBot()
        if request.method == 'POST':
            query = request.POST.get('query')
            #To check if the last quary is same as the new 
            chatobj=chat.objects.last()
            if chatobj:
                if query == chatobj.query:
                    pass
            elif len(query)>0:
                #Getting responce from ChatBot instance or a backup text
               
                responce = alpha.get_response(query) 
                try:
                    nameQuery = "make a single line(max characters 50) title for this '"+query+"' "
                    cbName = alpha.get_response(nameQuery)
                    print(cbName)
                except:
                    cbName = query
                
                #chat logics 
                Chat=chat(query=query,responce=responce)
                Chat.save()
                chatId=Chat.id
                
                Chatbase = chat.objects.all()

                tdate = timezone.now()
                
                chatBaseIns = chatBase(date=tdate,name=cbName)
                chatBaseIns.save()
                cB=chatBaseIns.id

                chat_instance = chat.objects.get(id=chatId)

                chatBaseIns.chats.set([chat_instance])
                
                print("chat base created with a chatid", chatId)
                st.pchats.add(chatBaseIns)
                
                return redirect(f"/student/doubts/{cB}/")
  
        return render(request,'student/doubts.html',{'st':st,'rCB':reveCB})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">404 Not-found</h1></body>')
    
def doubts_C(request,cB):
    st=isSession(request)
    if st!=None:
        #ChatBot instance
        alpha = ChatBot()
        cBase = chatBase.objects.get(id=cB)
        cBchats = cBase.chats.all()
        
        if request.method == 'POST':
            query = request.POST.get('query')
            #To check if the last quary is same as the new 
            chatobj=chat.objects.last()
            if query == chatobj.query:
                pass
            elif len(query)>0:
                #Getting responce from ChatBot instance or a backup text
                #responce = "hello mera api work nahi kr raha hai so , i cant respond to your queries now , i am very sorry !!"
                responce = alpha.get_response(query)
                
                #chat logics 
                Chat=chat(query=query,responce=responce)
                Chat.save()
                cBase.chats.add(Chat)
                
                Chatbase = chat.objects.all()
                return render(request,'student/doubts_C.html',{'st':st,'chat':cBchats,'sId':st,'cB':cBase,'cBid':cB})
  
        return render(request,'student/doubts_C.html',{'chat':cBchats,'st':st,'cB':cBase,'cBid':cB})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">404 Not-found</h1></body>')
    """ 
def batches(request):
    st=isSession(request)
    if st!=None:
        #to get all the batch which is registered by student 
        stBatch=st.sBatch.all()
        # excluding all the batch which is registered by student 
        batches=batch.objects.all()
        
        

        return render(request,'student/batches.html',{'st':st,'batch':batches})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">404 Not-found</h1></body>')
    
def settings(request):
    st=isSession(request)
    if st!=None:
        return render(request,'student/settings.html',{'st':st})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">404 Not-found</h1></body>')

def changePass(request):
    st=isSession(request)
    if st!=None:
        passUpdated=False
        if request.method == 'POST':
            oldPass=request.POST.get('oldPass')
            newPass =request.POST.get('newPass')
            if oldPass==st.pswrd:
                st.pswrd=newPass
                st.save()
                passUpdated=True
            else:
               return HttpResponse('<script>alert("Old Password doesnot Match  "); location.href="/student/settings/changePass/";</script>')
                    
            
        return render(request,'student/changePass.html',{'st':st,'passUpdated':passUpdated})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%); text-align:center;">404 Not-found <br> Or <br> Session Expired </h1></body>')

def complain(request):
    st=isSession(request)
    if st!=None:
        if request.method == 'POST':
            email = request.POST.get('email')
            comp = request.POST.get('complain')
            newComp = complaint(email=email, complain=comp)
            newComp.save()

                
        return render(request,'student/complain.html',{'st':st})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%); text-align:center;">404 Not-found <br> Or <br> Session Expired </h1></body>')
    
def profile(request):
    st=isSession(request)
    if st!=None:
        return render(request,'student/profile.html',{'st':st})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%); text-align:center;">404 Not-found <br> Or <br> Session Expired </h1></body>')
    
def editProfile(request):
    st=isSession(request)
    if st!=None:
        updated=False
        if request.method=='POST':
            fname=request.POST.get('fname')
            lname=request.POST.get('lname')
            phone=request.POST.get('phone')
            hqualification=request.POST.get('qualification')
            college=request.POST.get('college')
            address=request.POST.get('address')
            image=request.FILES.get('image')

            st.fname=fname
            st.lname=lname
            st.phone=phone
            st.qualification=hqualification
            st.college=college
            st.address=address
            if image!=None:
                st.image=image
            st.save()
            updated=True


        return render(request,'student/editProfile.html',{'st':st,'up':updated})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">404 Not-found <br> Or <br> Session Expired </h1></body>')
    
def logout(request):
    del request.session['sId']
    return redirect('homePage')

def myBatches(request):
    st=isSession(request)
    if st!=None:
        batches=st.sBatch.all()
        return render(request,'student/myBatches.html',{'st':st,'batch':batches})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">404 Not-found</h1></body>')
    
def viewBatch(request,bId):
    st=isSession(request)
    if st!=None:
        batches=batch.objects.get(id=bId)
        notification=batches.notifications.last()
        return render(request,'student/viewBatch.html',{'st':st,'b':batches,'notify':notification})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">404 Not-found</h1></body>')
    
def buyBatch(request,bId):
    st=isSession(request)
    if st!=None:
        batches=batch.objects.get(id=bId)

        return render(request,'student/buyBatchPage.html',{'st':st,'b':batches})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">404 Not-found</h1></body>')
    
def paymentGateway(request,bId):
    st=isSession(request)
    if st!=None:
        paid=False
        wrongPass=False

        batches=batch.objects.get(id=bId)
       
        if request.method=='POST':
            pswrd=request.POST.get('pass')

            if pswrd==st.pswrd:
                st.sBatch.add(batches)
                wrongPass=False
                paid=True
            else :
                paid=False
                wrongPass=True

        return render(request,'student/paymentgateway.html',{'st':st,'b':batches,'paid':paid,'wrong':wrongPass})
    else:
        return HttpResponse('<body bgcolor="black"><h1 style="color:blue;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);">404 Not-found</h1></body>')
    