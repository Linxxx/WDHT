from django.shortcuts import render
from django.http import  HttpResponse, JsonResponse
# Create your views here.

from django.template import loader, Context
from socket import socket, AF_INET, SOCK_STREAM

import sys,importlib
import json
from django.views.decorators.csrf import csrf_protect
import pingjia as pj

importlib.reload(sys)

def client(content):
    sock = socket(AF_INET, SOCK_STREAM)
    # sock.connect(('192.168.1.252',50008))
    sock.connect(('127.0.0.1',50008))

    sock.send(bytes(content,encoding='utf8'))

    # sock.send(content)
    reply = sock.recv(40960)
    sock.close()
    print('client got:[%s]' % reply)
    return reply


def index2(request):

    return render(request,'ZWGX/index.html')
    # return render(request,'index.html')

def index(request):

    return render(request,'index21.html')

@csrf_protect
def submit(req):
    question = ''
    if req.POST:
        if 'Question' in req.POST:
            question = req.POST['Question']
            print(question)
            print ("===")
            if question.strip()=='':
                print (question)
                question = '无'
            print ("===")
    answer = client(question.strip())
    print (answer)
    # return JsonResponse(answer)
    return HttpResponse(answer, content_type = 'application/json')

def submit2(req):
    # t = loader.get_template("index21.html")
    question = ''
    if req.POST:
        if 'Question' in req.POST:
            question = req.POST['Question']
            print(question)
            print ("===")
            if question.strip()=='':
                print (question)
                question = '无'
            print ("===")
    answer = client(question.strip())

    print (answer)
    # return HttpResponse(answer)
    # return render(req, "ZWGX/index.html", {'Answer': answer, 'Question': question})
    return render(req, "index21.html", {'Answer': answer, 'Question':question})

def pingfen(req):
    if req.POST:
        if 'grade' in req.POST:
            grade = req.POST['grade']
        if 'schoolname' in req.POST:
            schoolname = req.POST['schoolname']
        if 'intention' in req.POST:
            intention = req.POST['intention']
        if 'index' in req.POST:
            index = req.POST['index']
        if 'answer' in req.POST:
            answer = req.POST['answer']
        pj.PingFen(schoolname,intention,index,grade,answer)
    return HttpResponse("OK", content_type = 'application/text')

def fankui(req):
    if req.POST:
        if 'qfeedback' in req.POST:
            qfeedback = req.POST['qfeedback']
        if 'afeedback' in req.POST:
            afeedback = req.POST['afeedback']
        pj.FanKui(qfeedback,afeedback)
    return HttpResponse("OK", content_type = 'application/text')