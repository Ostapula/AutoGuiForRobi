import pyautogui
import time

currentMouseX, currentMouseY = pyautogui.position() # поточне перебування мишки на екрані
print(f"Current location: {currentMouseX, currentMouseY}")

scriptRestarted = 0 
icon_opened =  False 

pageDDOS = 'https://stop-russian-desinformation.near.page/'

def opneBrowser(): # функція для відкритя бравзера тілльки 1 раз
    pyautogui.doubleClick(1860, 30)
    print("Browser opened!")
    time.sleep(10)
    
def restartUser():
    pyautogui.click(1766, 84)   # настик на кнопку "змінити користувача"
    print('Browser change user 1')
    time.sleep(20)
    pyautogui.click(1417, 625)  # настиск на підтвердження про закриття
    print('Browser chage user 2')
    time.sleep(10)


def pasteURL(): # функція для написання (вставляння) посилання в url-bar
    pyautogui.click(1289, 85)
    pyautogui.press('backspace')  
    pyautogui.write(pageDDOS, interval=0.15)
    time.sleep(0.5)
    # pyautogui.hotkey('ctrl', 'v') для вставляння посилання
    pyautogui.press('enter')
    print("Link pasted! RUSSIA IS DDOSING!!!")

def cyclicTimer(): # функція для зациклення скрипту
    global scriptRestarted
    global icon_opened
    if icon_opened == False: # перевірка, що бравзер був відкритий
        opneBrowser()
        icon_opened = True
    pasteURL()     
    time.sleep(3600) # таймер роботи бравзера (3600 секунд = 1 годин)
    scriptRestarted += 1
    print(f"Script restarted: {scriptRestarted} times!")
    restartUser()
    cyclicTimer()  

if __name__ == '__main__':
    cyclicTimer()