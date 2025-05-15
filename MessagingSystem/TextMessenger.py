import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def server_log_in(server,port,email,password):
    SMTP_SERVER = server
    SMTP_PORT = port
    EMAIL_ADDRESS = email
    EMAIL_PASSWORD = password
    return [SMTP_SERVER, SMTP_PORT, EMAIL_ADDRESS, EMAIL_PASSWORD]

def create_recepient(number,carrier):
    recepient = number
    carrier_gateway =carrier
    return f'{recepient}{carrier}'



def create_message(text,message_sender,message_reciever,message_subject):
    message = MIMEText(text,'plain','utf-8')
    message['From'] = message_sender
    message['To'] = message_reciever
    message['Subject'] = message_subject
    return message

def send_message(server,port,email_address,email_password,reciever,message):
    try:
        with smtplib.SMTP(server, port) as server:
            server.starttls()
            server.login(email_address, email_password)
            server.sendmail(email_address, reciever, message.as_string())
        print("SMS sent successfully!")
    except Exception as e:
        print("Error sending SMS:", e)

"""
SMTP_SERVER = "smtp.gmail.com"  # Use your email provider's SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = "amjprogramming@gmail.com"
EMAIL_PASSWORD = "jpvr imgo vbck vhkt"

recepient_number = '2252767707'
carrier_gateway = "@txt.att.net"

sms_email = f'{recepient_number}{carrier_gateway}'
message = MIMEText("this is a test of the email to sms system, do not be afraid")
message['From'] = EMAIL_ADDRESS
message['To'] = sms_email
message['Subject'] = "SMS alert"

try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, sms_email, message.as_string())
    print("SMS sent successfully!")
except Exception as e:
    print("Error sending SMS:", e)
"""
def main():
    SMTP_SERVER = "smtp.gmail.com"  # Use your email provider's SMTP server
    SMTP_PORT = 587
    EMAIL_ADDRESS = "amjprogramming@gmail.com"
    EMAIL_PASSWORD = "jpvr imgo vbck vhkt"
    recepient_number = '2252767707'
    carrier_gateway = "@txt.att.net"

    credentials = server_log_in(SMTP_SERVER, SMTP_PORT, EMAIL_ADDRESS, EMAIL_PASSWORD)
    receiver = create_recepient(recepient_number,carrier_gateway)
    text = 'Modularization text, code successfully modularized, cannot display extra chars'
    subject = 'modularization test'
    message = create_message(text,credentials[2],receiver,subject)
    send_message(credentials[0],credentials[1],credentials[2],credentials[3],receiver,message)

if __name__ == '__main__':
    main()