from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from board.models import Question, Answer
from board.forms import QuestionForm, AnswerForm

def index(request):
    #질문 목록
    question_list = Question.objects.all()  #db 전체조회
    return render(request, 'board/question_list.html',
                  {'question_list':question_list})
    #return HttpResponse("pyweb 사이트 입니다.")

def detail(request, question_id):
    # 질문/답변 상세
    question = Question.objects.get(id=question_id) #해당 id의 질문
    return render(request, 'board/detail.html', {'question':question})

def question_create(request):
    #질문 등록
    if request.method == "POST":
        form = QuestionForm(request.POST)   #자료 전달받음(request.POST)
        if form.is_valid():
            question = form.save(commit=False) #가저장(날짜가 없어서 가저장)
            question.create_date = timezone.now() #날짜 시간 저장
            question.save()  #실제 저장
            return redirect('board:index') #이동할 경로(앱 네임사용) 저장
    else:
        form = QuestionForm()   #form 객체 생성
    return render(request, 'board/question_form.html', {'form':form})

def answer_create(request, question_id):
    #답변 등록
    question = Question.objects.get(id=question_id) #해당 id의 질문 객체 생성
    if request.method == "POST":
        form = AnswerForm(request.POST) #입력값 전달받음
        if form.is_valid():
            answer = form.save(commit=False)  #내용만 저장됨
            answer.create_date = timezone.now() #작성일
            answer.question = question  #외래키 질문 저장
            answer.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form= AnswerForm()
    context = {'question':question,'form':form}
    return render(request, 'board/detail.html', context)
