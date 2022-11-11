import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "Email"
    password = os.environ.get("PASSWORD")
    receiver = "Email"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)