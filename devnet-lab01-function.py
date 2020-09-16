# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:13:57 2020

@author: admin
"""


def hienthi_ten():
    print("Ten toi la Phong")
    
hienthi_ten()

def cong2so(x,y):
    tong = x + y
    print('X:{0}'.format(x))
    print('Y:{0}'.format(y))
    print("Tong 2 so "+ str(x) + " va " + str(y) + " la " + str(tong))
    
cong2so(100,200)


def chia2so(x,y):
    if type(x) == int and type(y) == int:
        if y == 0:
            print("Khong duoc chia cho 0")
        else :
            thuong = x / y
            print('So bi chia:{0}'.format(x))
            print('So chia:{0}'.format(y))
            print("Thuong 2 so la " + str(thuong))
    else :
        print("Gia tri dau vao khong hop le")

chia2so("name",0)