#移动鼠标
# coding=uft-8
from Lid.BeautifulReport3 import BeautifulReport
import unittest
import os
import time
import pyautogui
test_suite = unittest.defaultTestLoader
report_file = BeautifulReport(test_suite).output_report()
img_path = os.path.abspath('{}'.format(BeautifulReport.img_path))
# pyautogui.moveTo(960,80)
time.sleep(5)
#获取鼠标的位置
try:
    while True:
        x,y = pyautogui.position()
        print(x,y)
        if (x,y) == (960,80):
            break
except KeyboardInterrupt:
    print("\nExit.")
print(report_file)
print(img_path)