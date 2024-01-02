from dotenv import load_dotenv
import os
import pywhatkit
from datetime import datetime, timedelta
from time import sleep
import pyautogui

def next_friday():
    current_date = datetime.now()
    days_until_friday = (4 - current_date.weekday() + 7) % 7
    next_friday_date = current_date + timedelta(days=days_until_friday)

    return next_friday_date

load_dotenv()

location = os.getenv("LOCATION")
day_of_the_event = os.getenv("DAY_OF_THE_WEEK")
hour = os.getenv("HOUR")
price = os.getenv("PRICE")
pix_key = os.getenv("PIX_KEY")
pix_owner = os.getenv("PIX_OWNER")
contact_id = os.getenv("CONTACT_ID")
mode = os.getenv("MODE")

next_friday_date = next_friday()
date = next_friday_date.strftime("%d/%m/%Y")
message = f"Confirmem presença \n{location}, {date} {day_of_the_event} {hour} \n\n*VALOR ADIANTAMENTO *: *R$ {price}* \n*CHAVE PIX*: {pix_key}\n*RESPONSAVEL CHAVE*: _*{pix_owner}*_\n_Colocou o nome na lista faz o PIX_\n\n-Jordhan\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-Reservas\n-\n-\n-\n-\n-\n-"

if mode == "contact":
    pywhatkit.sendwhatmsg_instantly(contact_id, message)
    sleep(2)    
    seta =pyautogui.locateCenterOnScreen('src/seta.png')
    sleep(2)
    pyautogui.click(seta[0], seta[1])
    sleep(2)
elif mode == "group":
    pywhatkit.sendwhatmsg_to_group_instantly(group_id=contact_id, message=message, tab_close=True)
else:
    print("Erro ao enviar mensagem.")

print("Sucesso!")