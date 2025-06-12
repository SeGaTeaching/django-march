from django.db import models

# Create your models here.
class Example(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    views_count = models.IntegerField(default=10)
    is_published = models.BooleanField(default=False)
    gender = models.CharField(max_length=100, choices=[
        ("F", "Weiblich"),
        ("M", "Männlich"),
        ("D", "Divers")
    ])
    
    def __str__(self):
        return self.title
    
class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="Fragetext")
    pub_date = models.DateTimeField(auto_now=True, verbose_name="Veröffentlichungsdatum")
    
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Zugehörige Frage")
    choice_text = models.CharField(max_length=200, verbose_name="Antworttext")
    votes = models.IntegerField(default=0, verbose_name="Stimmen")
    
    def __str__(self):
        return self.choice_text
