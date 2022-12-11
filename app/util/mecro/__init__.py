from schedule import every, run_pending
from app.core.schedule.service import fill_this_week_schedule

every().monday.do(fill_this_week_schedule)

while True:
    run_pending()