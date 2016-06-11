from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Student, Predmet, Ocena

from django import template
register = template.Library()
# Create your views here.
class IndexView(generic.ListView):
    template_name='index.html'
    context_object_name='lista_ocena'
   
    def get_queryset(self):
        return Ocena.objects.all()
        
class ViewStudenti(generic.ListView):
    template_name='studenti.html'
    context_object_name='lista_studenata'
   
    def get_queryset(self):
        return Student.objects.all()
        
class DetailView(generic.DetailView):
    model = Ocena
    template_name='detail.html'
    
class DetailViewStudent(generic.DetailView):
    model = Student
    template_name='detailStudent.html'  
    
class DetailViewPredmet(generic.DetailView):
    model = Predmet
    template_name='detailPredmet.html'  
         

class ViewPredmeti(generic.ListView):
    template_name='predmeti.html'
    context_object_name='lista_predmeta'
    def get_queryset(self):
        return Predmet.objects.all()
        
def getOcena(request, predmetid, studentid):
    if request.method == 'GET':
        s=get_object_or_404(Student, pk=studentid)
        p=get_object_or_404(Predmet, pk=predmetid)     
        o=Ocena.objects.all()
        response_data=o.filter(predmet_id=p.id, student_id=s.id)
        HttpResponse(response_data)
        #return JsonResponse({'ocena': response_data,}) 
        #render(request, 'detailPredmet%s/' %predmetid, {'ocena': response_data,})
@register.filter
def dajOcenu(predmetid, studentid):
        s=Student.objects.get(id=studentid)
        p=Predmet.objects.get(id=predmetid)
        o=Ocena.objects.all()
        result=o.filter(predmet_id=p.id, student_id=s.id) 
        return {'ocena': result}        

