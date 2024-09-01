from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('message', views.sendMessage, name='sendmessage'),
    path('#section_1',views.index, name='section_1'),
    path('#section_2',views.index, name='section_2'),
    path('#section_3',views.index, name='section_3'),
    path('#section_4',views.index, name='section_4'),
    path('#section_5',views.index, name='section_5'),
    path('#section_6',views.index, name='section_6'),
    path('#section_7',views.index, name='section_7'),
    path('quantity',views.quantity, name='quantity'),

    path('auth', views.LoginApp.as_view(), name="auth"),
    path('register', views.SignUp.as_view(), name="register"),
    path('lk', views.Lk, name='lk'),
    path('getDataUser',views.getDataUser),
    path('getBronUser',views.getBronUser),
    path('getEquipment',views.getEquipment),
    path('logout', views.LogoutApp.as_view(), name="logout"),
    path('data',views.testdata),
    path('getOborud', views.GetOborud),
    path('getBron',views.GetBron),
    path('getPeref',views.GetPeref),
    path('saveBron',views.SaveBron),
    path('getBronAll',views.GetBronAll),
    path('getTourCsGo',views.getTourCsGo),
    path('RegisterTour',views.RegisterTour),
    path('checkToRegister',views.checkToRegister),
    path('RegisterBackTour',views.RegisterBackTour),
    path('getTourUser',views.getTourUser),
    path('getNameTour',views.getNameTour),
    path('getCloseBron', views.getCloseBron),
    path('changePassword', views.changePassword),
    path('saveNumber', views.saveNumber),
    path('checkNumber', views.checkNumber)



]
