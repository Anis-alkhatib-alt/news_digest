from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
import ssl

USERNAME = "alkhatib.anis@gmail.com"
PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
HOST = "smtp.gmail.com"
PORT = 465
RECEIVER = "alkhatib.anis@gmail.com"
CONTEXT = ssl.create_default_context()


def send_email(message):
    msg = MIMEMultipart()
    msg["From"] = USERNAME
    msg["To"] = RECEIVER
    msg["Subject"] = "Today's News"

    msg.attach(MIMEText(message.encode("utf-8"), "plain", "utf-8"))

    with smtplib.SMTP_SSL(HOST, PORT, context=CONTEXT) as server:
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME, RECEIVER, msg.as_string())


if __name__ == "__main__":
    send_email()
