'''
练习3————工程包
按照电子时钟显示时间的函数show()已给出如下，请编写主函数，
合理使用功能函数和time库，实现每隔1秒刷新一次时间的简易时钟。
（提示：可能用到的方法有：sleep()、localtime()、os.system('cls')）
'''
import time
import os

def show(hour, minute, second):
    """显示时间，例14:45:23"""
    return '%02d:%02d:%02d' % (hour, minute, second)

def main():
    
