import pyautogui as pg
import time


def hold_key(hold_time, hold_key):
    import time, pyautogui
    start = time.time()
    while time.time() - start < hold_time:
        pg.press(hold_key)


def giggity():
    time.sleep(3)
    hold_key(10, 'w')
    hold_key(1, 'e')


giggity()
