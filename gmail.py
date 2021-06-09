import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import service_builder
import userpass


def send_email(subject, email_msg):
    service = service_builder.service()

    mime_message = MIMEMultipart()
    mime_message["to"] = userpass.get_email_address()
    mime_message["subject"] = subject
    mime_message.attach(MIMEText(email_msg, "plain"))
    raw_string = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()

    message = service.users().messages().send(userId="me", body={"raw": raw_string}).execute()
    print("SENT: ")
    print("SUBJECT: " + subject)
    print(email_msg)
    print(message)

