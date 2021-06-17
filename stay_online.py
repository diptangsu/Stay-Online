import pyautogui
from time import perf_counter

MOVE_AMOUNT = 10  # px
SLEEP_THRESHOLD = 3  # seconds

def move_mouse():
    pyautogui.moveRel(-MOVE_AMOUNT, 0)
    pyautogui.moveRel(0, -MOVE_AMOUNT)
    pyautogui.click()
    pyautogui.moveRel(MOVE_AMOUNT, 0)
    pyautogui.moveRel(0, MOVE_AMOUNT)

x_, y_ = pyautogui.position()
start = perf_counter()

while True:
    x, y = pyautogui.position()
    pos = f'X: {x:<5} Y: {y:<5}'
    print(pos, end='')
    print('\b' * len(pos), end='', flush=True)

    now = perf_counter()
    # ASSUMPTION: human mouse use, movement > 10 px
    if abs(x - x_) > MOVE_AMOUNT or abs(y - y_) > MOVE_AMOUNT:
        x_, y_ = x, y
        start = now
    elif now - start >= 3:
        move_mouse()
