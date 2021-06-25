import time
import os

def show(hour, minute, second):
    """显示时间，例14:45:23"""
    return '%02d:%02d:%02d' % (hour, minute, second)

def main():
    while True:
        localtime = time.localtime()
        hour = int(localtime[3])
        minute = int(localtime[4])
        second = int(localtime[5])
        print(show(hour, minute, second))
        time.sleep(1)
        os.system('cls')

main()

