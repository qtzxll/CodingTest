# coding = utf-8

# Write a program to find out if two circles C1 and C2 are overlapped with each other.

import math

# 接收用户输入的两圆的圆心位置和半径
x1, y1 = eval(input("input the center of the first circle x,y："))
r1 = float(input("input the radius of the first circle:"))
x2, y2 = eval(input("input the center of the second circle:x,y："))
r2 = float(input("input the radius of the second circle:"))

d = math.hypot(x1 - x2, y1 - y2)  # 求圆心距

if d < abs(r1 - r2):
    print("两圆内切")
elif d == abs(r1 - r2):
    if r1 == r2:
        print("两圆重合")
    else:
        print("两圆内切")

elif d < r1 + r2:
    print("两圆相交")
elif d == r1 + r2:
    print("两圆外切")
else:
    print("两圆外离")
