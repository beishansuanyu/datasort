import tkinter as tk
from base64 import encode, decode
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()
f_path = filedialog.askopenfilename()

file = open(f_path, 'rb')
file_name =f_path.split('.')[0]
file.seek(0,2)
eof = file.tell()
file.seek(0,0)
data = file.read()
t_temp1 = 0

f2 = open("模拟通道数据数据004.txt",'w+')

files = [file,f2]

def write(item):

    a =0
    strs = str('{:.6f}'.format(t_temp1))
    for i in range(16):
        dat = item[a:a+2]
        dat = int.from_bytes(dat, byteorder='big', signed=True)
        # x = dat & 0x8000
        # y = dat & 0x7fff
        m = 2 ** 15
        # if x == 0:
        #     y = y
        # else:
        #     y = y - m
        # match i:
        #     case 0 | 2| 12| 14 :
        #         y = y*1
        #     case 1| 3| 4| 5| 6| 7| 8| 9| 10| 11| 13| 15:
        #         y = y
        #     case _:
        #         print('匹配到其他通道')
        y = dat / m * 10
        formatted_num = '{:.6f}'.format(y)
        str1 = '\t'+ str(formatted_num)
        strs =strs +str1
        a = a + 2
    f2.write(strs+'\n')
    



n = 0

while n <eof:
    write(data[n:n+32])
    n = n + 32
    print('\r' + "{:.2f}".format(n / 1000000) + '/' + "{:.2f}".format(eof / 1000000), end='', flush=True)

for m in files:
    m.close()


print("helloworld")