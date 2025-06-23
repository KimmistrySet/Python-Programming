import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
import os
import logging
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Email configuration
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
TWILIO_RECIPIENT_NUMBER = os.getenv('TWILIO_RECIPIENT_NUMBER')


# Function to send email
def send_email(subject, body, to_email=None):
    if to_email is None:
        to_email = EMAIL_USER  # Default to the user email
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USER, to_email, msg.as_string())
            logging.info("Email sent.")
    except smtplib.SMTPException as e:
        logging.error("Failed to send email: %s", e)
# Function to send SMS


def send_sms(body, to_phone=None):
    if to_phone is None:
        to_phone = TWILIO_RECIPIENT_NUMBER  # Default to the recipient number
    if not all([
        TWILIO_ACCOUNT_SID,
        TWILIO_AUTH_TOKEN,
        TWILIO_PHONE_NUMBER,
        to_phone
    ]):
        logging.error(
            "Twilio configuration is incomplete. Please check your "
            "environment variables."
        )
        return
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=body,
            from_=TWILIO_PHONE_NUMBER,
            to=to_phone
        )
        logging.info("SMS sent: %s", message.sid)
    except ImportError as e:
        logging.error("Twilio library is not installed: %s", e)
    except Exception as e:
        from twilio.base.exceptions import TwilioRestException
        if isinstance(e, TwilioRestException):
            logging.error("Failed to send SMS: %s", e)
        else:
            raise


if __name__ == "__main__":
    email_subject = "Auto Response"
    email_body = "This is a test email sent from the auto_respond script."
    sms_body = "This is a test SMS sent from the auto_respond script."

    send_email(email_subject, email_body)
    send_sms(sms_body, None)  # None will use the default recipient number
    logging.info("Auto respond script executed successfully.")
   