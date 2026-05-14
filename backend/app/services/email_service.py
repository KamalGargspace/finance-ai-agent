import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

from datetime import datetime

from app.config import (
    EMAIL_ADDRESS,
    EMAIL_PASSWORD
)

from app.database import SessionLocal

from app.models.audit_log import AuditLog


def send_real_email(

    invoice,

    generated_email
):

    try:

        subject = generated_email[
            "subject"
        ]

        body = generated_email[
            "body"
        ]

        recipient = invoice.email


        # Email setup
        message = MIMEMultipart()

        message["From"] = EMAIL_ADDRESS

        message["To"] = recipient

        message["Subject"] = subject

        message.attach(
            MIMEText(body, "plain")
        )


        # SMTP server
        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        server.starttls()

        server.login(
            EMAIL_ADDRESS,
            EMAIL_PASSWORD
        )

        server.sendmail(
            EMAIL_ADDRESS,
            recipient,
            message.as_string()
        )

        server.quit()


        # Save audit log
        db = SessionLocal()

        audit = AuditLog(

            invoice_no=invoice.invoice_no,

            client_name=invoice.client_name,

            email=invoice.email,

            stage=invoice.followup_stage,

            subject=subject,

            send_status="Sent",

            timestamp=str(
                datetime.now()
            )
        )

        db.add(audit)

        invoice.status = "Sent"

        db.commit()

        db.close()

        return {
            "message": "Email sent successfully"
        }

    except Exception as error:

        print(error)

        return {
            "message": "Email sending failed"
        }