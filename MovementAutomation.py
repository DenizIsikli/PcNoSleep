import random

import pyautogui as cursor

def movementAutomation():
  x, y = cursor.size()

  cursor.countdown(5)

  while True:

    x1 = random.randint(0, x)
    y1 = random.randint(0, y)

    cursor.moveTo(x1, y1)
    cursorInfo = cursor.getInfo()


    print(cursorInfo)

if __name__ == '__main__':
  movementAutomation()