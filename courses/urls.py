from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index),
    path('list', views.kurslar),
    path('<kurs_name>', views.details), 
    path('category/<int:categoy_id>', views.getCoursesByCategoryById),   
    path('category/<str:category_name>', views.getCoursesByCategory, name='courses_by_category'),
    ]


    


