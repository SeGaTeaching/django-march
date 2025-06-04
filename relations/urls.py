from django.urls import path
from . import views

urlpatterns = [
    path('', views.relations, name="relations"),
    path('students-list/', views.student_list, name="student_list"),
    path('students/<int:student_id>', views.student_detail, name="student_detail"),
    path('authors/', views.author_list, name="author_list"),
    path('authors/<int:author_id>', views.author_detail, name="author_detail"),
    path('dtl/', views.dtl_example, name="dtl_example"),
]
