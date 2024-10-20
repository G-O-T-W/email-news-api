import smtplib
import os
import ssl


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

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg=message)


