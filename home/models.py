from django.db import models
import smtplib
from email.message import EmailMessage
# from home.views import Contact



# Create your models here.
class Contact(models.Model):
    null=True
    name_surname=models.CharField(max_length=40)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    message=models.TextField()
    date=models.DateField()
    def __str__(self):
     return self.email

class Project(models.Model):
    projectimg=models.ImageField()
    protitle=models.CharField(max_length=30)
    prodescrip=models.CharField(max_length=400)
    prolink=models.URLField()

print(Project.prolink)


# tovar='vystudent68@gmail.com'
# subjectvar=f'A New Contact us message is arrived from{models.TextField()} '
# bodyvar=input('Enter the main message!!\n')

# def email_alert(to,subject,body):
#     msg=EmailMessage()
#     msg.set_content(body)
#     msg['subject']=subject
#     msg['to']=to
    
#     user ='spadeftw2@gmail.com'
#     password ='zrsuaynsgufiidpt'
#     msg['from']=user

#     server=smtplib.SMTP("smtp.gmail.com",587)

#     server.starttls()
#     server.login(user,password)
#     server.send_message(msg)
#     server.quit

# if __name__ == '__main__':
#     email_alert(tovar,subjectvar,bodyvar)






