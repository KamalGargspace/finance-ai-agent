from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException

import pandas as pd
import json

from app.database import SessionLocal

from app.models.invoice import Invoice
from app.models.audit_log import AuditLog

from app.utils.helpers import (
    calculate_overdue_days,
    determine_followup_stage
)

from app.services.ai_service import (
    generate_followup_email
)
from app.services.email_service import (
    mock_send_email
)

from app.services.email_service import (
    send_real_email
)

router = APIRouter()


@router.get("/test")
def test_api():

    return {
        "status": "API Working Successfully"
    }


@router.post("/upload-csv")
async def upload_csv(
    file: UploadFile = File(...)
):

    df = pd.read_csv(file.file)

    db = SessionLocal()

    uploaded = []

    for _, row in df.iterrows():

        overdue_days = calculate_overdue_days(
            row["due_date"]
        )

        followup_stage = determine_followup_stage(
            overdue_days
        )

        existing_invoice = db.query(
            Invoice
        ).filter(
            Invoice.invoice_no == row["invoice_no"]
        ).first()

        if existing_invoice:
            continue

        invoice = Invoice(

            invoice_no=row["invoice_no"],

            client_name=row["client_name"],

            amount=row["amount"],

            due_date=row["due_date"],

            email=row["email"],

            overdue_days=overdue_days,

            followup_stage=followup_stage
        )

        db.add(invoice)

        uploaded.append(
            row["invoice_no"]
        )

    db.commit()

    db.close()

    return {
        "message": "CSV uploaded successfully",
        "uploaded": uploaded
    }

@router.get("/invoices")
def get_invoices():

    db = SessionLocal()

    invoices = db.query(Invoice).all()

    results = []

    for invoice in invoices:

        results.append({

            "id": invoice.id,

            "invoice_no": invoice.invoice_no,

            "client_name": invoice.client_name,

            "amount": invoice.amount,

            "due_date": invoice.due_date,

            "email": invoice.email,

            "overdue_days": invoice.overdue_days,

            "followup_stage": invoice.followup_stage,

            "status": invoice.status
        })

    db.close()

    return results


@router.get("/generate-email/{invoice_id}")
def generate_email(invoice_id: int):

    db = SessionLocal()

    invoice = db.query(Invoice).filter(
        Invoice.id == invoice_id
    ).first()

    if not invoice:

        raise HTTPException(
            status_code=404,
            detail="Invoice not found"
        )

    generated_email = generate_followup_email(
        invoice
    )

    return {

        "invoice_no": invoice.invoice_no,

        "client_name": invoice.client_name,

        "email": invoice.email,

        "followup_stage":
        invoice.followup_stage,

        "generated_email":
        generated_email
    }


@router.post("/send-email/{invoice_id}")
def send_email(invoice_id: int):

    db = SessionLocal()

    invoice = db.query(Invoice).filter(
        Invoice.id == invoice_id
    ).first()

    if not invoice:

        raise HTTPException(
            status_code=404,
            detail="Invoice not found"
        )

    generated_email = generate_followup_email(
        invoice
    )

    result = send_real_email(

        invoice,

        generated_email
    )

    db.close()

    return {
        "message": result["message"]
    }

@router.get("/audit-logs")
def get_audit_logs():

    db = SessionLocal()

    logs = db.query(AuditLog).all()

    results = []

    for log in logs:

        results.append({

            "id": log.id,

            "invoice_no": log.invoice_no,

            "client_name": log.client_name,

            "email": log.email,

            "stage": log.stage,

            "subject": log.subject,

            "send_status":
            log.send_status,

            "timestamp":
            log.timestamp
        })

    db.close()

    return results        

@router.get("/analytics")
def analytics():

    db = SessionLocal()

    total_invoices = db.query(
        Invoice
    ).count()

    sent_invoices = db.query(
        Invoice
    ).filter(
        Invoice.status == "Sent"
    ).count()

    escalated = db.query(
        Invoice
    ).filter(
        Invoice.followup_stage ==
        "Escalation Required"
    ).count()

    pending = total_invoices - sent_invoices

    db.close()

    return {

        "total_invoices":
        total_invoices,

        "sent_invoices":
        sent_invoices,

        "pending_invoices":
        pending,

        "escalated":
        escalated
    }    

@router.get("/health")
def health_check():

    return {
        "status": "healthy"
    }    