import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP2GO settings
SMTP_SERVER = "mail.smtp2go.com"
SMTP_PORT = 587  # Use 465 for SSL, 587 for STARTTLS
USERNAME = st.secrets["SMTP_USER"]
PASSWORD = st.secrets["SMTP_PASS"]

st.title("Send Email via SMTP2GO")

# Input fields
sender_email = st.text_input("Sender Email", "lead@goodlife.dk")
receiver_email = st.text_input("Receiver Email", "jb@goodlife.dk")
subject = st.text_input("Subject", "Test Email from SMTP2GO")
body = st.text_area("Body", "Hello,\n\nThis is a test email sent using SMTP2GO and Python.")

if st.button("Send Email"):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(USERNAME, PASSWORD)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        st.success("Email sent successfully!")
    except Exception as e:
        st.error(f"Failed to send email: {e}")
