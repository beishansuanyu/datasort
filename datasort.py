import struct

import tkinter as tk
from base64 import encode
from tkinter import filedialog
import os
root = tk.Tk()
root.withdraw()
f_path = filedialog.askopenfilename()
t_temp1 = 0
t_temp2 = 0
t_temp3 = 0
t_temp4 = 0
t_temp5 = 0
t_temp6 = 0
t_temp7 = 0
t_temp8 = 0


file = open(f_path, 'rb')
file_name =f_path.split('.')[0]
file.seek(0,2)
eof = file.tell()
file.seek(0,0)
data = file.read()
f = open(file_name+"处理后结果.dat", "wb+")
f0 = open("通道1数据.txt",'w+',encoding='utf-8')
f1 = open("通道2数据.txt",'w+')
f2 = open("通道3数据.txt",'w+')
f3 = open("通道4数据.txt",'w+')
f4 = open("通道5数据.txt",'w+')
f5 = open("通道6数据.txt",'w+')
f6 = open("通道7数据.txt",'w+')
f7 = open("通道8数据.txt",'w+')
files = [f,f0,f1,f2,f3,f4,f5,f6,f7]


fs = 1000000
def write16(item,k,t_temp):
    i = 0
    while i <= 1087:
        dat = data[k:k+2]
        dat = int.from_bytes(dat, byteorder='big')
        # dat = dat /2**16*40-20
        t_temp = t_temp + 1
        m = 2 ** 15

        x = dat & 0x8000
        y = dat & 0x7fff

        if x == 0:
            y = y
        else:
            y = y - m

        y = y / m * 10

        str1 = '\t'.join([str(t_temp), str(y)]) + '\n'
        item.write(str1)
        k = k+2
        i = i+1
    return t_temp


def write32(item,k,t_temp):
    i = 0
    while i <= 543:
        dat_b = data[k:k+4]
        dat = int.from_bytes(dat_b, byteorder='big')

        t_temp = t_temp + 1
        m1 = 2**17

        x = dat & 0x00008000
        y1 = dat & 0x30000000
        y2 = dat & 0x00007fff
        y = (y2<<2) + (y1>>30)

        if x == 0 :
            y = y
        else:    y= y-m1

        y = y/m1*10

        str1 = '\t'.join([str(t_temp), str(y)])+'\n'
        item.write(str1)

        k = k+4
        i = i+1
    return t_temp


def match_example(item,m1):
    match item:
        case 0:
            global t_temp1
            t_temp1=write32(f0, m1,t_temp1)
        case 1:
            global t_temp2
            t_temp2=write32(f1, m1,t_temp2)
        case 2:
            global t_temp3
            t_temp3=write16(f2, m1,t_temp3)
        case 3:
            global t_temp4
            t_temp4=write16(f3, m1,t_temp4)
        case 4:
            global t_temp5
            t_temp5=write16(f4, m1,t_temp5)
        case 5:
            global t_temp6
            t_temp6=write16(f5, m1,t_temp6)
        case 6:
            global t_temp7
            t_temp7=write16(f7, m1,t_temp7)
        case 7:
            global t_temp8
            t_temp8=write16(f7, m1,t_temp8)
        case _:
            print("匹配到其他情况")




pattern = b'\x1a\xcf\xfc\x1d'
n = 0
while n <eof:
    m = data.find(pattern,n,eof)
    if m != -1:
        f.write(data[m:m + 2184])
        tongdao = data[m+7]
        match_example(data[m+7],m+8)
    else:
        break
    n=m+2184



while file in files:
    file.close()


print("helloworld")

# result = struct.unpack('format string', data)