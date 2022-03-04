from pyautogui import *
import pyautogui
import time 
import sys

ddosPage = 'https://stop-russian-desinformation.near.page/' #Посилання для DDOS

counterTimes = 0 # Змінна для підрахунку запуску повторення головної ф-ції (main)
closeNum = 0 # Змінна для підрахунку незнаходжених "Close img" (closeFunc)
def closeFunc(): # Функція для закривання бравзера
    global closeNum
    closeImg = pyautogui.locateCenterOnScreen('closetor.png', confidence = 0.8) # Картинка: "хрестик для закривання бравзера"
    if closeImg != None:
        pyautogui.click(closeImg)
        print(f'\'Close img\' founded on {closeImg}!')
    else:
        print('Counldn\'t found the \'Close img\'.')
        if closeNum == 1:
            sys.exit()
        else:
            closeNum = 1
            return
    time.sleep(5)

def openFunc(): # Функція для відкривання бравзера
    iconImg = pyautogui.locateCenterOnScreen('icontor.png', confidence = 0.7) # Картинка: "іконка бравзера"
    if iconImg != None:
        pyautogui.doubleClick(iconImg)
        print(f'\'Icon img\' founded on {iconImg}!')
    else:
        print('Counldn\'t found the \'Icon img\'.')
        sys.exit()
    time.sleep(15)

def searchFunc(): # Фуншкція для вводу посилання
    searchImg = pyautogui.locateCenterOnScreen('searchtor.png', confidence = 0.6) # Картинка: "пошукової панелі"
    if searchImg != None:
        pyautogui.click(searchImg)
        print(f'\'Search img\' founded on {searchImg}!')
        pyautogui.write(ddosPage, interval=0.01)
        time.sleep(0.5)
        pyautogui.press('enter')
    else:
        print('Counldn\'t found the \'Search img\'.')
        sys.exit()
    
def main(): # Головна функція для послідовної активації функцій вище й закицлення
    global counterTimes
    closeFunc()
    openFunc()
    searchFunc()
    time.sleep(3600) # таймер роботи бравзера (3600 секунд = 1 годин)
    counterTimes += 1
    print(f'Script was repeated: {counterTimes}.')
    main()
    
if __name__ == '__main__': # зациклення бота
    main()