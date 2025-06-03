from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Example

# Create your views here.
def polls(request):
    
      
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        is_published = request.POST.get("is_published")
        views_count = request.POST.get("views_count")
        gender_choice = request.POST.get("gender")
                
        q = Example(
            title=title,
            content=content,
            views_count=views_count,
            is_published=bool(is_published),
            gender=gender_choice
        )
        q.save()
        
        return HttpResponse(
            f"""
            <h2>yo, die Daten passen so weit:</h2>
            <p>title: {q.title}</p>
            <p>content: {q.content}</p>
            <p>gender: {q.gender}</p>      
            """)
        
    
    return render(request, "polls/polls.html", {
        "gender_choices": [
            ("F", "Weiblich"),
            ("M", "Männlich"),
            ("D", "Divers")
        ]
    })
    

def example_detail_view(request, pk):
    
    q = get_object_or_404(Example, pk=pk)
    context = {
        'page_title': f'Example "{q.title}" bearbeiten (Manuell)',
        'is_update': True # Optional: um im Template anders zu reagieren
    }
    
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        views_count = request.POST.get('views_count')
        is_published = request.POST.get('is_published')
        gender = request.POST.get('gender')
        
        q.title = title
        q.content = content
        q.views_count = views_count
        q.is_published = bool(is_published)
        q.gender = gender
        q.save()
        
        return HttpResponse("success")
    
    form_data = {
        "title": q.title,
        "content": q.content,
        "views_count": q.views_count,
        "is_published": q.is_published,
        "gender": q.gender
    }
    context["form_data"] = form_data
    
    context["gender_choices"] = [
            ("F", "Weiblich"),
            ("M", "Männlich"),
            ("D", "Divers")
        ]
    
    return render(request, "polls/polls.html", context)