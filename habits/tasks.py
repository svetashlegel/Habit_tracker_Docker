from datetime import datetime
from habits.models import Habit
from users.services import tg_send_message
from habits.services import check_current_day
from celery import shared_task


@shared_task(name="send_habits")
def send_habits():
    current_time = datetime.now()
    for habit in Habit.objects.filter(is_pleasant=False):
        # DAILY HABIT
        if habit.frequency == "DAILY":
            if habit.time.strftime("%H:%M") == current_time.strftime("%H:%M"):
                chat_id = habit.owner.chat_id
                if habit.award:
                    users_award = habit.award
                else:
                    users_award = habit.link_pleasant.action
                message = (f"Трекер полезных привычек. Напоминание.\nДействие: {habit.action}\nМесто: {habit.place}"
                           f"\nПродолжительность: {habit.duration} мин.\nВаше вознаграждение: {users_award}")
                tg_send_message(chat_id, message)
        # WEEK DAY HABIT
        else:
            today = check_current_day()
            if habit.frequency == today:
                if habit.time.strftime("%H:%M") == current_time.strftime("%H:%M"):
                    chat_id = habit.owner.chat_id
                    if habit.award:
                        users_award = habit.award
                    else:
                        users_award = habit.link_pleasant.action
                    message = (f"Трекер полезных привычек. Напоминание.\nДействие: {habit.action}\nМесто: {habit.place}"
                               f"\nПродолжительность: {habit.duration} мин.\nВаше вознаграждение: {users_award}")
                    tg_send_message(chat_id, message)
