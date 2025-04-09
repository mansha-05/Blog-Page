import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv('MAIL_ID')
my_password = os.getenv('MAIL_PASSWORD')


def send_email(name, email, phone, message):
    email_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    msg = MIMEText(email_message, "plain", "utf-8")
    msg["Subject"] = "New Message from Contact Form"
    msg["From"] = formataddr(("Website Contact", my_email))
    msg["To"] = my_email
    msg["Reply-To"] = email

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=msg.as_string()
        )
