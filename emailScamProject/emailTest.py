import smtplib

# Define email details
FROM = 'ascamprojectforclass@gmail.com'
TO = ["czu002@email.latech.edu"]  # lList of emails
SUBJECT = "Hello!"
TEXT = "This message was sent with Python's smtplib."

# Prepare actual message
message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

# Send the mail using Gmail's SMTP server
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail's SMTP server
    server.starttls()  # Secure the connection
    server.login(FROM, "nlrf sncc gskx lbqf")  # App Password Email
    server.sendmail(FROM, TO, message)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()
