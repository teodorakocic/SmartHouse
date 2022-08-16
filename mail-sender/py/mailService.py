import smtplib
import ssl

port = 587  
smtp_server = "smtp-mail.outlook.com"

sender = "smarthouseassistant@outlook.com"
recipient = "teakocic99@gmail.com"
sender_password = "SmartAssistant2022"

message = """\nIf You want to track the consumption of electric energy in Your smart home, also for more information about how much energy You have used in last week, month, year in Your smart house, visit the http://localhost:5000 page.\n\nSmart House Assistant"""

SSL_context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=SSL_context)
    server.login(sender, sender_password)
    server.sendmail(sender, recipient, message)
