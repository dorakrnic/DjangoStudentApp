# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 19:39:03 2016

@author: Isidora
"""
from student.models import Student, Predmet, Ocena
from django import template
register = template.Library()

@register.filter
def getOcena(value, arg):
        s=Student.objects.get(id=arg) 
        o=Ocena.objects.all()
        strOcena=str(o.filter(predmet_id=value, student_id=s.id))
        sliceOcena=strOcena[9:10]
        return sliceOcena
        
@register.filter
def dodajjedan(value):
    return value+1;        

#u template-u load --> {% load my_tags %}
#u template-u se poziva npr {{ student.id|dodajjedan}} to je model.objekat|filter