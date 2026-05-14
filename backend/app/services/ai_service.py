import google.generativeai as genai
import json

from app.config import GEMINI_API_KEY

# Configure Gemini
genai.configure(
    api_key=GEMINI_API_KEY
)

# Load Gemini Model
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_followup_email(invoice):

    stage = invoice.followup_stage

    tone_map = {

        "Stage 1 - Warm":
            "Warm and Friendly",

        "Stage 2 - Polite":
            "Polite but Firm",

        "Stage 3 - Formal":
            "Formal and Serious",

        "Stage 4 - Stern":
            "Stern and Urgent",

        "Escalation Required":
            "Escalation Notice"
    }

    tone = tone_map.get(stage)

    prompt = f"""
You are a professional finance collections assistant.

Generate a payment follow-up email.

Tone:
{tone}

Invoice Details:
- Client Name: {invoice.client_name}
- Invoice Number: {invoice.invoice_no}
- Amount Due: ₹{invoice.amount}
- Due Date: {invoice.due_date}
- Days Overdue: {invoice.overdue_days}

Requirements:
- Write professionally
- Include a clear CTA
- Return ONLY valid JSON

JSON format:
{{
    "subject": "...",
    "body": "..."
}}
"""

    response = model.generate_content(
        prompt
    )

    cleaned_response = response.text.strip()

    # Remove markdown if Gemini adds it
    cleaned_response = cleaned_response.replace(
        "```json",
        ""
    ).replace(
        "```",
        ""
    )

    parsed_response = json.loads(
        cleaned_response
    )

    return parsed_response