from apscheduler.schedulers.background import (
    BackgroundScheduler
)

from app.scheduler.jobs import (
    auto_send_reminders
)

scheduler = BackgroundScheduler()

# Run every 1 minute
scheduler.add_job(

    auto_send_reminders,

    "interval",

    minutes=1
)