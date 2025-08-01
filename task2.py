# -*- coding: utf-8 -*-
"""task2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vQGuMwoqOBKs3DiYUNyHSNCiJQNcQW8O
"""

# تعريف الوظائف الأساسية
def move_forward(steps):
    print(f"الروبوت يتحرك للأمام {steps} خطوات")

def turn_right(degrees):
    print(f"الروبوت يدور يمين {degrees} درجة")

def turn_left(degrees):
    print(f"الروبوت يدور يسار {degrees} درجة")

def stop():
    print("الروبوت يتوقف")

def pick_item(item):
    print(f"الروبوت جمع {item}")

def wait(seconds):
    print(f"انتظار {seconds} ثواني")

# الخوارزمية الرئيسية
def warehouse_robot_task():
    print("ابدأ المهمة")
    move_forward(5)
    stop()
    pick_item("تمر")
    wait(2)
    turn_right(90)
    move_forward(3)
    stop()
    pick_item("ماء")
    wait(2)
    turn_left(180)
    move_forward(8)
    stop()
    print("انتهت المهمة")

# تشغيل المهمة
warehouse_robot_task()