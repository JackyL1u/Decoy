import smtplib
import ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from decouple import config
import pathlib


def send_email(message):
    filename = str(pathlib.Path(__file__).parent.resolve()) + "/../temp_files/picture.jpg"
    port = 465
    sender = config("EMAIL_USERNAME")
    passw = config("EMAIL_PASSWORD")
    receive = sender
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["to"] = receive
    msg["Subject"] = "Decoy Alert"
    msg.attach(MIMEText(message, "plain"))
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {filename}", )
    msg.attach(part)
    text = msg.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, passw)
        server.sendmail(sender, receive, text)