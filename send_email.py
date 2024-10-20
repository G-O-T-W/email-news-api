import smtplib
import os
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(message):
    """
        This function sends an email using SMTP protocol.

        Note:
        This function uses the SMTP_SSL protocol to connect to the Gmail SMTP server.
        It retrieves the sender's credentials from environment variables.
        The receiver's email address is hardcoded.
        """

    host = "smtp.gmail.com"
    port = 465

    # Sender's credentials
    username = "rishavdiyali@gmail.com"
    password = os.getenv("PASSWORD")

    # Receiver's email
    receiver = "diyali.rishav.22@gmail.com"

    # Create a MIMEText object with the message body
    email_message = MIMEMultipart()
    email_message["From"] = username
    email_message["To"] = receiver
    email_message["Subject"] = "Daily News"

    # Attach the email body with UTF-8 encoding
    body = MIMEText(message, "plain", "utf-8")
    email_message.attach(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg=email_message.as_string())


