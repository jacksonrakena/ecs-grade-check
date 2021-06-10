import base64
from os.path import isfile
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import service_builder
import config

CREDENTIALS_FILE = "credentials.json"


def init():
    """
    Check for the credentials file
    :return:
    """
    if not isfile(CREDENTIALS_FILE):
        print("WARNING: A 'credentials.json' file was not found. This means that GetGrade will not be able to send "
              "emails. Please download your credentials file from google for gmail.")


def send_email(subject, email_msg):
    """
    Send an email
    :param subject: the subject
    :param email_msg: the message to send
    :return:
    """
    service = service_builder.service()

    mime_message = MIMEMultipart()
    mime_message["to"] = config.get_email_address()
    mime_message["subject"] = subject
    mime_message.attach(MIMEText(email_msg, "plain"))
    raw_string = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()

    message = service.users().messages().send(userId="me", body={"raw": raw_string}).execute()
    print("SENT: ")
    print("SUBJECT: " + subject)
    print(email_msg)
    print(message)
