import pyautogui
import time

def moverRaton():
    while True:
        print("Parriba..")
        pyautogui.dragRel(-100, -100, duration = 1)
        time.sleep(30)
        print("Pabajo..")
        pyautogui.dragRel(100, 100, duration = 1)
        time.sleep(30)

if __name__ == "__main__":
    print("Trae pa' ca' el raton...")
    try:
        moverRaton()
    except:
        print("Taluego!")
    finally:
        exit()