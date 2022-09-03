import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Smart house notification"
body = "If You want to track the consumption of electric energy in Your smart home, also for more information about how much energy You have used in last week, month, year in Your smart house, visit the http://localhost:5000 page.\n\nSmart House Assistant"
sender_email = "smarthouseassistant@outlook.com"
receiver_email = "teakocic99@gmail.com"
password = "SmartAssistant2022"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email 

message.attach(MIMEText(body, "plain"))

filename = "mail-sender\instruction.pdf" 

with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
 
encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

message.attach(part)
text = message.as_string()

SSL_context = ssl.create_default_context()

with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
    server.starttls(context=SSL_context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)