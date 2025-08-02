import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_notification(ticket):
    sender_email = 'tarunbantupalli1947@gmail.com'
    receiver_email = 'tarunbantupalli1947@gmail.com'  # could be yours for testing
    password = 'njdfygdcuzfnhpbs'

    subject = f"[New Ticket] {ticket.title}"
    body = f"""A new ticket has been submitted:

Title: {ticket.title}
Category: {ticket.category}
Priority: {ticket.priority}
Status: {ticket.status}
"""

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Notification sent.")
    except Exception as e:
        print("Error sending email:", e)
