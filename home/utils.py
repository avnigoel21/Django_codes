
from django.conf import settings
from django.core.mail import send_mail

def send_mail_to_client():
    subject = "Interview Result"
    message = "You are selected!!"
    from_email = settings.EMAIL_HOST_USER
    recipent_list = ["avnigoel98@gmail.com" , 'achimote2021@gmail.com']
    send_mail(subject, message, from_email, recipent_list)