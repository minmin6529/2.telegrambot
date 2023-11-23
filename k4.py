import telegram
import schedule
import time
import pytz
import datetime

token = "5803209467:AAETECsh3bpVlLJXRCEbkvyf2PQxaQ8_LUY"
public_chat_name = '@mj2test'

def send_message(message):
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=public_chat_name, text=message)

def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    current_hour = now.hour
    if 6 <= current_hour < 23:
        send_message(f"Current time: {current_time}")
    else:
        print("Sleeping...")
    
schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)