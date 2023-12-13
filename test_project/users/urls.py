from django.urls import path
from . import views 

urlpatterns = [


    path('', views.index, name='index'),
    
    path('contact', views.contact, name='contact' ),
    path('freshers_job', views.freshers_job, name='freshers_job' ),
    path('experience_job', views.experience_job, name='experience_job' ),
    path('fresherplacement', views.fresherplacement, name='fresherplacement'),
    path('experienceplacement', views.experienceplacement, name='experienceplacement' ),
    path('testimonial', views.testimonial, name='testimonial' ),
    path('compus', views.campus, name='campus' ), 

 ]