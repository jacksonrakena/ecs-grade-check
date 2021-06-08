import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import service_builder

service = service_builder.service()

emailMsg = "New grades for: "
mimeMessage = MIMEMultipart()
mimeMessage['to'] = 'isaacy2012@gmail.com'
mimeMessage['subject'] = 'You won'
mimeMessage.attach(MIMEText(emailMsg, 'plain'))
raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
print(message)

