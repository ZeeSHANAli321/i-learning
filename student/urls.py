
from django.urls import path
from . import views

urlpatterns = [
    
    path('base/', views.stDashboard),
    path('logout/', views.logout),
    
    path('dashboard/', views.dashboard),
    path('videoLectures/', views.videoLectures,name='videosLectures'),
    path('playVideo/<int:vId>/<int:bId>/', views.playVideo,name='playVideo'),
    path('assignments/', views.assignments,name='assignments'),
    #Removing Doubts ai as i dont have working api 
    #path('doubts/', views.doubts,name='doubts'),
    #path('doubts/<int:cB>/',views.doubts_C),
    path('eNotes/', views.eNotes,name='eNotes'),
    path('studyMaterials/', views.studyMaterials,name='studyMaterial'),
    path('batches/', views.batches,name='batches'),
    path('myBatches/', views.myBatches,name='myBatches'),
    path('viewBatch/<int:bId>/', views.viewBatch,name='viewBatch'),
    path('timings/', views.timings,name='timings'),
    path('profile/', views.profile,name='profile'),
    path('editProfile/', views.editProfile,name='editProfile'),
    path('settings/', views.settings,name='settings'),
    path('settings/changePass/', views.changePass,name='changePass'),
    path('settings/complain/', views.complain,name='complain'),
    path('buyBatch/<int:bId>/', views.buyBatch,name='buyBatch'),
    path('paymentGateway/<int:bId>/', views.paymentGateway,name='paymentGateway'),
    
    
]
