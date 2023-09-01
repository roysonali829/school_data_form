from django.shortcuts import render
from app.models import *

# Create your views here.

def insert_scdata(request):
    if request.method=='POST':
        scn = request.POST['scn']
        sp = request.POST['sp']
        sl = request.POST['sl']
        sco = School.objects.get_or_create(ScName=scn,ScPrincipal=sp,ScLocation=sl)[0]
        sco.save()
        QLSCO = School.objects.all()
        d = {'QLSCO':QLSCO}
        return render(request,'display_scdata.html',d)
    return render (request,'insert_scdata.html')

def insert_sdata(request):
    if request.method == 'POST':
        sc = request.POST['scn']
        sco = School.objects.get(ScName=sc)
        sn = request.POST['sn']
        si = request.POST['si']
        so = Student.objects.get_or_create(ScName=sco,SName=sn,Sid=si)[0]
        so.save()
        QLSO = Student.objects.all()
        d = {'QLSO':QLSO}
        return render(request,'display_sdata.html',d)
    return render (request,'insert_sdata.html')