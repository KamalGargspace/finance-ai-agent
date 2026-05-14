from datetime import datetime

def calculate_overdue_days(due_date):

    today = datetime.today()

    due = datetime.strptime(
        due_date,
        "%Y-%m-%d"
    )

    overdue_days = (today - due).days

    return max(overdue_days, 0)


def determine_followup_stage(overdue_days):

    if overdue_days <= 0:
        return "Not Due"

    elif overdue_days <= 7:
        return "Stage 1 - Warm"

    elif overdue_days <= 14:
        return "Stage 2 - Polite"

    elif overdue_days <= 21:
        return "Stage 3 - Formal"

    elif overdue_days <= 30:
        return "Stage 4 - Stern"

    else:
        return "Escalation Required"