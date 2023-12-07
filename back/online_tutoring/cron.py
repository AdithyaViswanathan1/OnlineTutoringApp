from django.core import mail
from django.conf import settings
from tutor.models import Tutor
from student.models import Student
from appointments.models import Appointments
import datetime

def dailyEmailReminder(): #Sends emails to students and tutors that have appointments on today's date
    connection = get_connection() #Establishes connection to mail server
    
    #Grab Querysets of appointments that match today's date
    studentappointments = Appointments.objects.filter(time=datetime.date.today()).order_by("student")
    tutorappointments = Appointments.objects.filter(time=datetime.date.today()).order_by("tutor")
    
    #Send email to all students with appointment matching today's date
    if studentappointments.exists():
        currentStudentId = studentappointments.first().student
        message = "This is a reminder from TutorUTD that you have the following tutoring appointments today: \n \n" 
        for e in studentappointments:
            if e.student!=currentStudentId:
                send_mail("Tutor UTD: Appointment Reminder",
                    message,
                    settings.EMAIL_HOST_USER,
                    [Student.objects.get(pk=currentStudentId).email], 
                    connection)
                currentStudentId = e.student
                message = "This is a reminder from TutorUTD that you have the following tutoring appointments today: \n \n" 
                
            message + " Appointment at time " + e.time + " for course " + e.course + " at " + e.location + " with tutor " + Tutor.objects.get(e.tutor).full_name + "\n"
    
    #Send email to all tutors with appointment matching today's date
    if tutorappointments.exists():
        currentTutorId = tutorappointments.first().tutor
        message = "This is a reminder from TutorUTD that you have the following tutoring appointments today: \n \n" 
        for e in tutorappointments:
            if e.tutor!=currentTutorId:
                send_mail("TutorUTD: Appointment Reminder",
                    message,
                    settings.EMAIL_HOST_USER,
                    [Tutor.objects.get(pk=currentTutorId).email], 
                    connection)
                currentTutorId = e.tutor
                message = "This is a reminder from TutorUTD that you have the following tutoring appointments today: \n \n" 
                
            message + " Appointment at time " + e.time + " for course " + e.course + " at " + e.location + " with student " + Student.objects.get(e.tutor).full_name + "\n"
    
    connection.close()