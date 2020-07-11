from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question
# Create views here.


def index(request):
    myname = "Mai Loi"
    taisan1 = ["May tinh","Dien thoai","Xe may","Nha o"]
    context = {"name" : myname , "taisan": taisan1}
    return render(request,"polls/index.html", context)


def test(request):
    return HttpResponse("Hello Wold")

def viewlist(request):
    List_question = Question.objects.all() #get_object_or_404(Question ,pk=1)
    context = {"dsquest": List_question }
    return render(request, "polls/questionlist.html", context)

def detailView(request,question_id):
    q = Question.objects.get(pk=question_id)
    return render(request,"polls/detail_question.html",{ "qs": q })

def vote(request,question_id):
    q = Question.objects.get(pk=question_id)
    try:
        dulieu= request.POST["choice"]
        c = q.choice_set.get(pk=dulieu)
    except:
        HttpResponse("Không có choice")

    c.vote=c.vote+1
    c.save()
    return render(request,'polls/result.html',{"q": q})

