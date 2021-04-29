import pyautogui
import time
# print('Press Ctrl-C to quit')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: {} Y: {}'.format(*[str(x).rjust(4) for x in [x, y]])
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')
while True:
    pyautogui.click(x=259, y=104, duration=2)
    time.sleep(1)