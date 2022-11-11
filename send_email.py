import smtplib
import ssl
import os


def send_email(message):
    host = "#"
    port =
    username = "#"
    password = os.environ.get("PASSWORD")
    receiver = "#"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)