from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django import template
register = template.Library()

# Create your models here.
class Student(models.Model):
    studentIme=models.CharField(max_length=15, verbose_name='Ime')
    studentPrezime=models.CharField(max_length=30, verbose_name='Prezime')
    index=models.CharField(max_length=10)
    grad=models.CharField(max_length=30, null=True)
    adresa=models.CharField(max_length=50, null=True)
    jmbg=models.CharField(max_length=13,unique=True)
    pol=models.CharField(max_length=1, null=True)
    datumRodjenja=models.DateField(auto_now=False, auto_now_add=False, null=True)  
    def __str__(self):
        return '%s %s' % (self.studentIme, self.studentPrezime)
 
class Predmet(models.Model):
    nazivPredmeta=models.CharField(max_length=50, verbose_name='Naziv predmeta')
    sifra=models.CharField(max_length=4)
    studenti=models.ManyToManyField(Student, through='Ocena')
    @register.simple_tag
    def getOcena(self, studentid):
        s=Student.objects.get(id=studentid) 
        o=Ocena.objects.all()
        return o.filter(predmet_id=self.id, student_id=s.id) 
    def __str__(self):
        return self.nazivPredmeta
       
class Ocena(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    predmet=models.ForeignKey(Predmet, on_delete=models.CASCADE)        
    ocena=models.IntegerField(default=0, validators=[MinValueValidator(6), MaxValueValidator(10)]) 
    def __str__(self):
        return str(self.ocena)

#manytomany se stavlja samo u jednoj od dve klase, django prepoznaje logiku (pr: pica, nadevi)