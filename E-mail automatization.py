import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText

email = EmailMessage()
email['From'] = '<suntsmurf@gmail.com>'
email['To'] = '<mihai.iacob2001@gmail.com>'
email['Subject'] = 'Email automat'
email.set_content("Acesta este un email trimis automat cu Python!")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("suntsmurf@gmail.com", "parola")
    smtp.send_message(email)

print("Email trimist cu succes!")