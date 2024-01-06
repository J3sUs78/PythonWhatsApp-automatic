import pywhatkit as pwk
#import pyautogui
from screenSize import 
import time

#define the recipient´s phone number (with country code) and message
phone_number = "+569 31384247"
message = "Hola, este es un mensaje automatizado"

#Send message
pwk.sendwhatmsg(phone_number,message, 0, 38) # Sends the messsage
time.sleep(15)

# Moves the cursor the the message bar in Whatsapp
#pyautogui.moveTo(992,457) 

#pyautogui.click()

# Sends the message
#pyautogui.press('enter') 

print("key pressed")
