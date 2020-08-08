from django.db import models

# Create your models here.
class todolist(models.Model):
    Title = models.CharField(max_length=50)#제목
    content = models.TextField()#내용
    Completion =models.BooleanField() #완료
    Date = models.DateTimeField('date Date') #날짜
    Writer = models.CharField(max_length=50) #작성자

