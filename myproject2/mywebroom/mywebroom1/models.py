from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('data published')

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Booking(models.Model):
    startDate = models.DateField()
    startTime = models.TimeField()
    endDate = models.DateField()
    endTime = models.TimeField()
    def __str__(self):
        return str(self.startDate)+","+str(self.startTime)+","+str(self.endDate)+","+str(self.endTime)
        # return "วันที่ :"+str(self.startDate)+"เริ่มตั้งแต่เวลา :"+str(self.startTime)+"ถึงวันที่ :"+str(self.endDate)+"จนถึงเวลา :"+str(self.endTime)
    
class Person(models.Model):
    name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    detail = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class Room(models.Model):
    room_number = models.CharField(max_length=50)
    # Add other room details as needed
    def __str__(self):
        return self.room_number