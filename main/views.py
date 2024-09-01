from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .models import Equipment,Periphery,Reservation,Tournament,PeopleTournament,Phone
import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage


def sendMessage(request):
    
    name = request.GET['name']
    email = request.GET['email']
    tema = request.GET['tema']
    message = request.GET['message']
    tema ='('+ name + ')' + tema
#     msg = EmailMessage(
#           subject=tema,
#           body=message,
#           from_email=settings.EMAIL_HOST_USER,
#           to=(settings.EMAIL_HOST_USER,),
#           headers={'From': settings.EMAIL_HOST_USER}
# )
#     msg.content_subtype = 'html'
#     msg.send()
    # headers = {'To': '{} <{}>'.format(name, email)}
    send_mail(tema, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
    return HttpResponse('true')


def index(request):


    return render(request, 'main/index.html')
#
# def auth(request):
#     return render(request, 'main/ticket.html')

# def register(request):
#     return render(request, 'main/register.html')

class SignUp(CreateView):
    model = User
    form_class = RegisterUserForm
    success_url = reverse_lazy("home")
    template_name = "main/register.html"
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        aut_user = authenticate(username=username,password=password)
        login(self.request, aut_user)
        return form_valid


class LoginApp(LoginView):
    form_class = AuthUserForm
    success_url = reverse_lazy("home")
    template_name = "main/ticket.html"
    def get_success_url(self):
        return self.success_url


class LogoutApp(LogoutView):
    next_page = reverse_lazy("home")
def checkNumber(request):
    if request.method == 'GET':
        UserId = request.GET['UserId']
        modelUser = User.objects.get(pk=UserId)
        modelPT = Phone.objects.all().filter(userPhone=modelUser)
        posts_serialized = serializers.serialize('json', modelPT)
        return JsonResponse(posts_serialized,safe=False)
def saveNumber(request):
   if request.method == 'GET':
       phone = request.GET['phone']
       UserId = request.GET['UserId']
       check = request.GET['check']
       modelUser = User.objects.get(pk=UserId)
       if check=='0':
        model = Phone.objects.create(userPhone=modelUser,phoneNumber=phone)
        return HttpResponse('true')
       else:
        model = Phone.objects.get(userPhone=modelUser)
        if model.phoneNumber == phone:
            return HttpResponse('one')
        else:
         model.phoneNumber = phone
         model.save()
         return HttpResponse('change')


def Lk(request):
    return render(request, 'main/lk.html')

def changePassword(request):
    if request.method == 'GET':
        old_password = request.GET['old_password']
        new_password = request.GET['new_password']
        UserId = request.GET['UserId']
        changePassUser = User.objects.get(pk=UserId)
        if changePassUser.check_password(old_password):
            changePassUser.set_password(new_password)
            changePassUser.save()
            return HttpResponse('true')
        else:
            return HttpResponse('false')

            
            

def getDataUser(request):
    if request.method == 'GET':
        idUserPk = request.GET['UserId']
        modelUser = User.objects.all().filter(pk=idUserPk)
        user_serialized = serializers.serialize('json',modelUser)
        return JsonResponse(user_serialized,safe=False)
    
def getBronUser(request):
    if request.method == 'GET':
        idUserPk = request.GET['UserId']
        modelUser = User.objects.get(pk=idUserPk)
        model = Reservation.objects.all().filter(user1=modelUser)
        user_serialized = serializers.serialize('json',model)
        return JsonResponse(user_serialized,safe=False)
    
def getEquipment(request):
    if request.method == 'GET':
        eq = request.GET['eq']
        modelEq = Equipment.objects.all().filter(pk=eq)
        eq_serialized = serializers.serialize('json',modelEq)
        return JsonResponse(eq_serialized,safe=False)

def getTourCsGo(request):
    if request.method == 'GET':
        number = request.GET['number']
        model = Tournament.objects.all().filter(gameTour=number)
        posts_serialized = serializers.serialize('json', model)
        return JsonResponse(posts_serialized,safe=False)

def RegisterTour(request):
    if request.method == 'GET':
        nameTour = request.GET['nameTour']
        authUserId = request.GET['authUserId']
        current_time = datetime.datetime.now()
        model_nameTour = Tournament.objects.get(nameTournament=nameTour)
        model_user1 = User.objects.get(pk=authUserId)
        comment1 = str(nameTour) + ' ' + str(authUserId) + '' + str(current_time) 
        model = PeopleTournament.objects.create(TournamentId=model_nameTour,date_register=current_time,
                                           comment=comment1,UserIdTour=model_user1)
        # posts_serialized = serializers.serialize('json', model)
        return HttpResponse('true')
def getTourUser(request):
    if request.method == 'GET':
        UserTour =  request.GET['UserId']
        UserId = User.objects.get(pk=UserTour)
        model = PeopleTournament.objects.all().filter(UserIdTour=UserId)
        user_serialized = serializers.serialize('json', model)
        return JsonResponse(user_serialized,safe=False)
def getNameTour(request):
    if request.method == 'GET':
     nameTour = request.GET['nameTour']
     model = Tournament.objects.all().filter(pk=nameTour)
     user_serialized = serializers.serialize('json', model)
     return JsonResponse(user_serialized,safe=False)
def getCloseBron(request):
    if request.method == 'GET':
        BronPk = request.GET['pk']
        delBron = Reservation.objects.get(pk=BronPk)
        delBron.delete()
        return HttpResponse('true')



def checkToRegister(request):
    if request.method == 'GET':
         userCheck = request.GET['userCheck']
         nameTour = request.GET['nameTour']
         model_nameTour = Tournament.objects.get(nameTournament=nameTour)
         modelPT = PeopleTournament.objects.all().filter(UserIdTour=userCheck,TournamentId=model_nameTour)
         posts_serialized = serializers.serialize('json', modelPT)
         return JsonResponse(posts_serialized,safe=False)

def RegisterBackTour(request):
    if request.method == 'GET':
         nameTour = request.GET['nameTour']
         authUserId = request.GET['authUserId']
         model_nameTour = Tournament.objects.get(nameTournament=nameTour)
         delUchastie = PeopleTournament.objects.get(UserIdTour=authUserId,TournamentId=model_nameTour)
         delUchastie.delete()
         return HttpResponse('true')

def testdata(request):
    if request.method == 'GET':
        number = request.GET['number']
        model = Equipment.objects.all().filter(number=number)
        posts_serialized = serializers.serialize('json', model)
        return JsonResponse(posts_serialized,safe=False)

def GetOborud(request):
    if request.method == 'GET':
        model = Equipment.objects.all()
        posts_serialized = serializers.serialize('json',model)
        return JsonResponse(posts_serialized,safe=False)

def quantity(request):
    if request.method == 'GET':
        cs2 = Tournament.objects.get(pk=1)
        dota2 = Tournament.objects.get(pk=2)
        warface = Tournament.objects.get(pk=3)
        result = {}
        model = PeopleTournament.objects.filter(TournamentId=cs2).count()
        model2 = PeopleTournament.objects.filter(TournamentId=dota2).count()
        model3 = PeopleTournament.objects.filter(TournamentId=warface).count()
        result['cs2']=(str(model))
        result['dota2']=(str(model2))
        result['warface']=(str(model3))
        # result = Tournament.objects.all()
        # quantity_serialized = serializers.serialize('json',result)
        return JsonResponse(result,safe=False)



def GetBron(request):
    if request.method == 'GET':
        number = request.GET['number']
        model = Reservation.objects.all().filter(equipment=number)
        reservation_serializaed = serializers.serialize('json',model)
        return JsonResponse(reservation_serializaed,safe=False)
def GetBronAll(request):
    if request.method == 'GET':
        model = Reservation.objects.all()
        reservation_serializaed = serializers.serialize('json',model)
        return JsonResponse(reservation_serializaed,safe=False)
def GetPeref(request):
    if request.method =='GET':
        model = Periphery.objects.all()
        peref_serialized = serializers.serialize('json',model)
        return JsonResponse(peref_serialized,safe=False)

def SaveBron(request):
    if request.method == 'GET':
        user_corrent = request.GET['user']
        user_corrent_int = int(user_corrent)
        start = request.GET['start']
        end = request.GET['end']
        equipment1 = request.GET['equipment']
        equipmentint = int(equipment1)
        peref = request.GET['peref']
        perefArr = peref.split("-")
        comment1 = request.GET['comment']
        model_equipment = Equipment.objects.get(pk=equipmentint)
        model_user1 = User.objects.get(pk=user_corrent_int)

        # for i in range()
        # if Reservation.objects.filter(equipment=model_equipment,user1=model_user1)
        model = Reservation.objects.create(equipment=model_equipment,time_start=start,end_date=end,
                                           comment=comment1,user1=model_user1)
        for el in perefArr:
            if not el=='':
             el1= int(el)
             model.periphery.add(el1)

        return HttpResponse('true')
    