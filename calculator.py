import pyautogui, sys, time

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()

        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

        print(positionStr, end='')

        print('\b' * len(positionStr), end='', flush=True)

        # pyautogui.moveTo(100, 150)

        #pyautogui.moveTo(1778, 1000)

        #pyautogui.scroll(10)

        #pyautogui.scroll(-10)

        pyautogui.moveRel(0, 100,1)

        #time.sleep(3)

        #pyautogui.moveRel(30, 0)

        #time.sleep(3)

        pyautogui.moveRel(0, -100,1)

        #time.sleep(3)

        #pyautogui.moveRel(-30, 0)

        #time.sleep(3)

        # pyautogui.moveRel(0, 10)

except KeyboardInterrupt:

    print('\n')





