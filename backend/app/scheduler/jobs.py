from app.database import SessionLocal

from app.models.invoice import Invoice

from app.services.ai_service import (
    generate_followup_email
)

from app.services.email_service import (
    mock_send_email
)


def auto_send_reminders():

    print("Running automated reminder job...")

    db = SessionLocal()

    invoices = db.query(Invoice).filter(
        Invoice.status != "Sent"
    ).all()

    for invoice in invoices:

        # Skip escalation cases
        if invoice.followup_stage == \
            "Escalation Required":

            print(
                f"Escalated: "
                f"{invoice.invoice_no}"
            )

            continue

        try:

            # Generate AI email
            generated_email = \
                generate_followup_email(
                    invoice
                )

            # Mock send
            mock_send_email(

                invoice,

                generated_email
            )

            print(
                f"Reminder sent for "
                f"{invoice.invoice_no}"
            )

        except Exception as error:

            print(
                f"Failed for "
                f"{invoice.invoice_no}"
            )

            print(error)

    db.close()