from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def main():
    def click(x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    # Color of button: (48,106,31)
    # (x=710, y=750)
    while True:
        with open('3names.txt') as f:
            for line in f:
                line = line.strip(' ').strip('\n')
                print(line)
                if keyboard.is_pressed('q') == False:
                    flag = 0
                    #x=1078, y=596

                    click(1078, 596)
                    pyautogui.write(line, interval=0.01)

                    pic = pyautogui.screenshot(region=(700, 740, 720, 760))

                    width, height = pic.size
                    #x=1078, y=596

                    r, g, b = pic.getpixel((710, 750))

                    if b == 31 and r == 49 and g == 106:
                        flag = 1
                        click(710, 750)
                        time.sleep(0.1)


if __name__ == '__main__':
    main()
