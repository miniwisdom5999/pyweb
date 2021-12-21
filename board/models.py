from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=100)  #제목 칼럼
    content = models.TextField()                #질문 내용
    create_date = models.DateTimeField()        #질문 작성일

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #외래키, 제목
    content = models.TextField()          #답변 내용
    create_date = models.DateTimeField()  #답변 작성일

    def __str__(self):
        return self.content