import pyautogui as p
import time


num = input('How many times do you want to send the Message: ')


what = input('What do you want to say?: ')

print('Move your cursor to the message box and click on it so that the cursor is flashing. Wait for the messages to '
      'start sending')

time.sleep(7)
for i in range(int(num)):
    p.typewrite(what)
    p.press("enter")

quit()
