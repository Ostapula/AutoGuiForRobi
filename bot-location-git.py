import pyautogui
import time

currentMouseX, currentMouseY = pyautogui.position() # поточне перебування мишки на екрані
print(f"Current location: {currentMouseX, currentMouseY}")

scriptRestarted = 0 

pageDDOS = 'https://stop-russian-desinformation.near.page/'

def closeBrowser(): # функція для закриття бравзера
    pyautogui.click(1795, 30)
    print("Browser closed!")
    time.sleep(5)

def openBrowser(): # функція для відкривання бравзера
    pyautogui.doubleClick(1860, 30)
    print("Browser opened!")
    time.sleep(12)

def pasteURL(): # функція для написання (вставляння) посилання в url-bar
    pyautogui.click(1345, 65)
    pyautogui.write(pageDDOS, interval=0.15)
    time.sleep(0.5)
    # pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    print("Link pasted! RUSSIA IS DDOSING!!!")

def cyclicTimer(): # функція для зациклення скрипту
    global scriptRestarted
    closeBrowser() # 1
    openBrowser()  # 2
    pasteURL()     # 3
    time.sleep(3600) # таймер роботи бравзера (3600 секунд = 1 годин)
    scriptRestarted += 1
    print(f"Script restarted: {scriptRestarted} times!")
    cyclicTimer()  # 4   

if __name__ == '__main__':
    cyclicTimer()