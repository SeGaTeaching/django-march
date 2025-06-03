from django.db import models

# Create your models here.

#-------------------------------------
# Foreign-Key: Viele zu Eins Beziehung
#-------------------------------------
class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    # Jedes Buch hat genau einen Autor
    # Wenn Autor gelöscht wird, dann wird wegen CASCADE auch das Buch bzw. die Bücher die mit dem Autor verknüpft sind gelöscht
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} by {self.author}" 


#--------------------------------------
# OneToOneField: Eins zu Eins Beziehung
#--------------------------------------
class Person(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 
    
    
class Passport(models.Model):
    pass_number = models.IntegerField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.pass_number} from {self.person}"


#------------------------------------------
# ManyToManyField: Viele zu Viele Beziehung
#------------------------------------------
class Student(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255)
    # Ein Kurs kann viele Studenten haben und Studenten können viele Kurse haben
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.title

#-----------------------
# Beispiel ManyToMany mit Through Tabelle Custom
#-----------------------
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    product = models.ManyToManyField(Product, through="Between")
    
    def __str__(self):
        return self.name

class Between(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    creation_date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.product.name} in {self.category.name}"
    
