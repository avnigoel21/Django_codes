
from django.conf import settings
from django.core.mail import send_mail, EmailMessage

def send_mail_to_client():
    subject = "Interview Result"
    message = "You are selected!!"
    from_email = settings.EMAIL_HOST_USER
    recipent_list = ["avnigoel98@gmail.com" , 'achimote2021@gmail.com']
    send_mail(subject, message, from_email, recipent_list)

def send_email_with_attachment(subject, message, recipent_list, file_path):
    mail = EmailMessage(subject= subject , body=message , from_email= settings.EMAIL_HOST_USER , to=recipent_list)
    mail.attach_file(file_path)
    mail.send()
