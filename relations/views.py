from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Student, Author

# Create your views here.
def relations(request):
    return HttpResponse("Hello")

def student_list(request):
    students = Student.objects.all()
    data = {}
    data["students"] = students
    
    return render(request, "relations/student_list.html", data)

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    courses = student.course_set.all()
    
    data = {"student": student, "courses": courses}
    
    return render(request, "relations/student_detail.html", data)

#----------------------
# Autoren Seiten Viewis
#----------------------

def dtl_example(request):
    
    context = {
        "name": "Franziska",
        "alter": 10,
        "hobbys": ["Tennis", "Golf", "Formel 1", "Wandern", "Kontrabass", "Dungeons and Dragons"],
        "fruit": ["apple", "banana", "kiwi", "mango"],
        "address": {
            "plz": 33442,
            "city": "Herzebrock-Clarholz"
        }
    }
    
    return render(request, "relations/dtl_example.html", context)

# Autoren Übersicht
def author_list(request):
    authors = Author.objects.all().order_by("name")
    one = Author.objects.get(pk=1)
    one_dict = one.__dict__
    
    context = {
        "authors": authors,
        "one_dict": one_dict
    }
    
    return render(request, "relations/author_list.html", context)

# Autoren Einzel Ansicht
def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    books = author.book_set.all()
   
    return render(request, "relations/author_detail.html", {
       "autor": author,
       "buecher": books,
    })
    