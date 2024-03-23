from django.shortcuts import render,HttpResponse,redirect
from.models import train,person,trip3,events,locations,plans,Trip_info,User,expense
from .forms import GroupForm,personForm,tripForm,EventsForm,planForm,ExpenseForm
from django.http import HttpResponseRedirect
from .booking_api import get_hotels
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .flights_api import flights
from .ai_done import ai
import pandas as pd
import json
import datetime
from datetime import datetime

# Create your views here.
def login1(request):

    return render(request,'blog/login.html')
@login_required
     
def home(request):
    data="hello"
    if request.method == "POST":
        content=request.POST.get('userInput')
        
        data=ai(str(content))

  
        print(data)
        return render(request,"blog/result.html",{'data':data})
    
    return render(request,"blog/chat_try.html")

    


    return render(request,'blog/flights.html')
@login_required
def view(request):
    data=train.objects.all()
    return render(request,'blog/login copy.html',{'data':data})
def logout1(request):
     logout(request)
     return redirect('login1')
@login_required

def viewf(request):
    submitted=False
    if request.method=="POST":
        form=GroupForm(request.POST)
        if form.is_valid():
            form.save()
            a=5
            return HttpResponseRedirect(f'/blog/viewf?submitted={a}')
    else:
            form=GroupForm
            if 'submitted' in request.GET:
                submitted= request.GET.get('submitted')
                

    return render(request,'blog/viewf.html',{'form':form,'submitted':submitted})
@login_required

def search_hotels(request):
    location = "Delhi"  # Get location from user input
    hotels_data = get_hotels(location)
    data_to_display = hotels_data.get('data', {})
    # Process hotels_data and pass it to your template
    return render(request, "blog/hotels.html", {"hotels": hotels_data})
@login_required

def flights1(request):
    data2=""
    submitted=False

     
    if request.method == "POST":
         
       
        flying_to=request.POST.get('flying_to')
        departing=request.POST.get('departing')
       
        adults=request.POST.get('adults')
       

      
         
      
       
        flights1=flights(flying_to,departing,adults)
        data=flights1.get('data',{})
        data2=data.get('flights',{})
        print(data2)
        return render(request,"blog/flights_result.html",{"data":data2})
    else:
         
            if 'submitted' in request.GET:
                submitted= request.GET.get('submitted')

    return render(request,"blog/flights.html")
    
        
       
        
         

         
         
         
    
     
     

def add_person(request):
    submitted=False
    if request.method=="POST":
        form=personForm(request.POST)
        if form.is_valid():
            form.save()
            a=5
            return HttpResponseRedirect(f'/blog/add_person?submitted={a}')
    else:
            form=personForm
            if 'submitted' in request.GET:
                submitted= request.GET.get('submitted')
                

    return render(request,'blog/add_person.html',{'form':form,'submitted':submitted})
from datetime import datetime,date,time
current_time = datetime.now()
def home2(request):
    op=Trip_info.objects.all() # if leader and user is same then problem
    user1=request.user.username
    l=[]
    future_events=[]
    current_datetime = datetime.now()
    future_events1 = events.objects.filter(date__gte=current_datetime.date()
                                          )
    for event in future_events1:
    # Combine the event date and time
        event_datetime = datetime.combine(event.date, event.s_time)
        if event_datetime >= current_datetime:
            future_events.append(event)
    
    
    day_events=[]
    iop=events.objects.all()
  
    u=User.objects.get(username=user1)
    io=Trip_info.objects.all()
    li=[]
    for i in io:
         if i.user == u:
              li.append(i)
 
    expense7=expense.objects.all()

  
    yu=[]# correct it
    yu1=[]# correct it
    
    for j in li:
        expense1=0
        exp_t=0
        
        for i in expense7:
            
            if i.user == j:
              expense1=expense1+i.expense
            if i.trip_id1 == j.trip :
             exp_t=exp_t+i.expense
                 
        yu.append(expense1)
        yu1.append(exp_t)
    trip_ids=[]
    future=[]
            
        
    for i in op:
         
         
         if i.user.username == user1 :
             
              
         
              l.append(i.trip)
              trip_ids.append(i.trip.id)
    
    for i in trip_ids:
        for j in iop:
            if (j.id1.trip_id.id == i):
                current_date=datetime.now().date()
                if (j.date == current_date):
                     day_events.append(j)
        for k in future_events:
            if(k.id1.trip_id.id == i):
                   future.append(k)
    

                
                     

              

              
   


    return render(request,'blog/index.html',{'trip':l,"user":request.user,"holidays":holidays(),"expense1":yu,"total":yu1,"future":future,"day_events":day_events})
def holidays():


    file_path = r'C:\Users\vyoma123\Desktop\planner\start\blog\holidays.xlsx'  # Replace with your actual file path

# Read data from both sheets
    xls = pd.ExcelFile(file_path)
    sheet1_df = pd.read_excel(xls, sheet_name='Table 1')
    sheet2_df = pd.read_excel(xls, sheet_name='Table 2')

# Initialize a list to store the results
    result_list = []

# Assuming your columns are in the order of Date and Reason
    for df in [sheet1_df, sheet2_df]:
        for row in df.itertuples(index=False):
            date, reason = row
            if not pd.isnull(date) and not pd.isnull(reason):
                result_list.append([date, reason])
    return result_list
def viewc(request):
    return render(request,'blog/viewc.html',{'holidays':holidays()})
def trips(request):
    op=Trip_info.objects.all()
    user1=request.user.username
    l=[]
    for i in op:
         if i.user.username == user1:
              l.append(i.trip)
    return render(request,'blog/trip.html',{'trip':l})
import random
def add_trip(request):
        submitted=False
        if request.method=="POST":
            form=tripForm(request.POST)
            if form.is_valid():
                form.save()
                user1=request.user
                trip_id_value = form.cleaned_data.get('id')
                uy=form.cleaned_data.get('leader')
                
                op=trip3.objects.get(id=trip_id_value)
                u=User.objects.get(username=request.user.username)
                t=User.objects.get(username=uy.username)
                if u == t :
                     
               
              
                    ut=Trip_info(user=t,trip=op,ty=random.randint(1, 1000))
                    ut.save()
                else:
                    ut=Trip_info(user=t,trip=op,ty=random.randint(1, 1000))
                    ut.save()

                    io=Trip_info(user=u,trip=op,ty=random.randint(1, 1000))
                    io.save()
                
              

                
                return HttpResponseRedirect(f'/blog/viewf?submitted=True')
        else:
            form=tripForm
            if 'submitted' in request.GET:
                submitted= request.GET.get('submitted')
                

        return render(request,'blog/add_trip.html',{'form':form,'submitted':submitted})




def trip_info1(request,trip_id):
     l=[]
     io=plans.objects.all()
     op=trip3.objects.get(id=trip_id)
     fo_plans=[]
     group=False
     if op.leader.username == request.user.username:
          group=True
   
     
    
          
     for i in io:
            if i.trip_id.id == trip_id:
                if i.followed == True:
                     fo_plans.append(i)
            


         
                l.append(i)
        
    
               
          
     return render(request,"blog/trip_info.html",{"plans":l,"group":group,"following":fo_plans,"trip_id":trip_id})
def event_info(request,event_id):
     l=[]
     
     op=events.objects.all()
     for i in op:
          
          if i.id1.id_plan == event_id:

            print("1")
            l.append(i)
          
               
            
        
    
     return render(request,"blog/event_info.html",{'event':l})
def add_plan(request,trip_id1):
        student1=Trip_info.objects.all()
        trip_id=trip3.objects.get(id=trip_id1)
        st=[]
        for i in student1:
             if User.objects.get(username=request.user.username) == i.user and i.trip == trip_id :
                  st=i
        submitted=False
        if request.method=="POST":
            form=planForm(request.POST,initial={'owner': st,"trip":trip_id})
            if form.is_valid():
                form.save()
                
                return HttpResponseRedirect(f'/blog/viewf?submitted=True')
        else:
            form=planForm(initial={'owner': st,"trip":trip_id})
            if 'submitted' in request.GET:
                submitted= request.GET.get('submitted')
                

        return render(request,'blog/add_plan.html',{'form':form,'submitted':submitted})
def add_event(request,trip_id1):
        submitted=False
        student1=Trip_info.objects.all()
        trip_id=trip3.objects.get(id=trip_id1)
        st=[]
        for i in student1:
             if User.objects.get(username=request.user.username) == i.user and i.trip == trip_id :
                  st=i
        

        if request.method=="POST":
            form=EventsForm(request.POST,initial={'owner': student1})
            if form.is_valid():
                form.save()
                
                return HttpResponseRedirect(f'/blog/viewf?submitted=True')
        else:
            form=EventsForm
            if 'submitted' in request.GET:
                submitted= request.GET.get('submitted')
                

        return render(request,'blog/add_events.html',{'form':form,'submitted':submitted})
def try1(request):
     op=trip3.objects.get(place="RISHIKESH")
     u=User.objects.get(username=request.user.username)

     io=Trip_info(user=u,trip=op)
     io.save()
     return HttpResponse(op)


def edit_profile(request,profile_id):
    u=User.objects.get(username=profile_id)
    if request.method == "POST":
          
          u.first_name=request.POST.get("f_name","")
          u.last_name=request.POST.get("l_name","")
          u.username=request.POST.get("bits_id","")
          u.age=request.POST.get("age","")
          u.user_mobile=request.POST.get("ph_number","")
          u.save()
          return redirect("home2")
    return render(request,"blog/edit_profile.html",{"data":u})
def trip_detail(request, trip_id):

    registered_users = Trip_info.objects.filter(trip=trip_id)
    return render(request, 'blog/user.html', { 'registered_users': registered_users})
"""def add_expense(request,trip_id):

    op=Trip_info.objects.all()
    l=[]
    for i in op:
          if i.trip.id == trip_id :
               l.append(i)
    if request.method =="POST":
         data = request.POST
         for i in data:
              if 'user_' in i:
                user_id = i.split('_')[1]
                
                user1= data['user_'+user_id]
                expense1 = data['expense_'+user_id]
                
           
                desc = int(data['desc'])
                op=expense(user=Trip_info.objects.get(user=),expense=expense1,expense1=desc)
                op.save()


             
                   

                
                
              
               
                
                
                
             
        
    return render(request,"blog/add_expense.html",{"data":l})

         
        """
def add_expense1(request,trip_id):
        io=Trip_info.objects.all()
        op=[]
        for i in io:
             if i.trip == trip3.objects.get(id=trip_id):
                  op.append(i.ty)
        print(op)
        

        

        submitted=False
        if request.method=="POST":
            form=ExpenseForm(request.POST,users=op,initial={'trip': trip3.objects.get(id=trip_id)})
            if form.is_valid():
                form.save()

                
                return HttpResponseRedirect(f'/blog/viewf?submitted=True')
        else:
          
            form=ExpenseForm(users=op,initial={'trip': trip3.objects.get(id=trip_id)})
            if 'submitted' in request.GET:
                submitted= request.GET.get('submitted')
                

        return render(request,'blog/add_expense1.html',{'form':form,'submitted':submitted,"trip_id":trip_id})
def add_friends(request):
        u=trip3.objects.all()
        ui=[]
        for i in u:
             if i.leader == User.objects.get(username=request.user.username):
                  ui.append(i.id)
        print(ui)
        

        submitted=False
        if request.method=="POST":
            form=GroupForm(request.POST,trips=ui)
            if form.is_valid():
                form.save()
                
                return HttpResponseRedirect(f'/blog/viewf?submitted=True')
        else:
            form=GroupForm(trips=ui)
            if 'submitted' in request.GET:
                submitted= request.GET.get('submitted')
                

        return render(request,'blog/add_friends.html',{'form':form,'submitted':submitted})
def expense1(request,trip_id):
     op=expense.objects.all()
     l=[]
     for i in op:
          print(i)
          if i.trip_id1.id == trip_id:
               print("hell")
               l.append(i)
     return render(request,"blog/expense.html",{"data":l})
def event_info1(request,event_id):
     l=[]
     
     op=plans.objects.get(id_plan=event_id)
     if op.owner.user.username == request.user.username :
          op.delete()
          return HttpResponse("deleted")
     else:
        return HttpResponse("NOT CREATOR OF THE PLAN")
        
  

   
               
            
        
    
     #return render(request,"blog/devent_info.html",{'event':l})
def follow(request,event_id):
     io=plans.objects.get(id_plan=event_id)
     io.followed=True
     io.save()
     return redirect('home2')
     






