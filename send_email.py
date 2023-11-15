import os
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

# # Load environment variables
# current_dir = Path.cwd()
# envars = current_dir / ".env"
# load_dotenv(envars)

# Read environment variables
sender_email = os.environ["EMAIL"]
password_email = os.environ["EMAIL_PASSKEY"]

current_date = datetime.datetime.now()
date_format = '%a %d %b %Y'
subject = current_date.strftime(date_format)

def send_emails(subject, receiver_email, name):

    body = f"""\
    Hi {name},
    I hope you are well.
    Please see the attached for today's summary of the prices of your essentials.
    Kind regards,
    Product Price Tracker
    """

    message = MIMEMultipart()
    message["From"] = formataddr(("Product Price Tracker", f"{sender_email}"))
    message["To"] = receiver_email
    message["BCC"] = sender_email
    message["Subject"] = subject
    
    message.attach(MIMEText(body, 'plain'))

    results_file = "results.csv"

    with open(results_file, 'rb') as email_attachment:

        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((email_attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename = " + results_file)
        message.attach(attachment_package)

        text = message.as_string()

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == "__main__":
    send_emails(
        subject=f"Products Price Summary - {subject}",
        name="Chisom",
        receiver_email=sender_email
    )
    os.remove("results.csv")