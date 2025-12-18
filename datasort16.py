import struct
# -*- coding: utf-8 -*-

import tkinter as tk
from base64 import encode, decode
from tkinter import filedialog
import os

from numpy.f2py.crackfortran import endifs
from numpy.ma.core import append
import matplotlib.pyplot as plt
import numpy as np

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
fs = 5000
f = open(file_name+"处理后结果.dat", "wb+")
f0 = open("数字通道1数据.dat",'wb')
f1 = open("数字通道2数据.dat",'wb')
f3 = open("数字通道3数据.dat",'wb')
f4 = open("数字通道4数据.dat",'wb')
f5 = open("数字通道开始时间.txt",'w+')
f6 = open("模拟通道数据.dat",'wb+')
time0 = [0]
time1 = [0]
time3 = [0]
time4 = [0]
f2 = open("模拟通道数据数据006拼帧.txt",'w+')
f7 = open("数据长度.txt",'w+')
f2.write('时间')
for i in range(16):
    f2.write('\t'+'通道'+str(i+1))
f2.write('\n')
num_temp= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

files = [file,f,f0,f1,f2,f3,f4,f5,f6,f7]
times = [time0,time1,time3,time4]

list_length = []
channel_cnt = 0



def write(item,m1):
    range1 = m1/2-1
    range1 = int(range1)
    # f2.write(str('{:.6f}'.format(t_temp1)))
    a =0
    for i in range(range1):
        global channel_cnt,t_temp1
        if channel_cnt  == 15:
            f2.write('\n'+str('{:.6f}'.format(t_temp1)))
            t_temp1 += 1
            channel_cnt = 0
        else:
            channel_cnt += 1
        dat = item[a:a+2]
        dat = int.from_bytes(dat, byteorder='big', signed=True)
        # if dat-num_temp[i] >7400 or dat-num_temp[i]<-7400:
        if dat > 22340 or dat < -22340:
            # dat = num_temp[i]
            dat = 0
        else:
            dat = dat
            # num_temp[i] = dat


        m = 2 ** 15

        # match i:
        #     case 0 | 2| 12| 14 :
        #         y = y*1
        #     case 1| 3| 4| 5| 6| 7| 8| 9| 10| 11| 13| 15:
        #         y = y
        #     case _:
        #         print('匹配到其他通道')
        y = dat / m * 22
        formatted_num = '{:.6f}'.format(y)
        str1 = '\t'+ str(formatted_num)
        f2.write(str1)
        a = a + 2

    # f2.write('\n')

def write_old(item,m1):
    range1 = m1/2-1
    range1 = int(range1)
    # f2.write(str('{:.6f}'.format(t_temp1)))
    a =0
    f2.write('\n' + str('{:.6f}'.format(t_temp1)))
    for i in range(range1):

        dat = item[a:a+2]
        dat = int.from_bytes(dat, byteorder='big', signed=True)
        # if dat-num_temp[i] >7400 or dat-num_temp[i]<-7400:
        if dat > 22340 or dat < -22340:
            # dat = num_temp[i]
            dat = 0
        else:
            dat = dat
            # num_temp[i] = dat


        m = 2 ** 15

        # match i:
        #     case 0 | 2| 12| 14 :
        #         y = y*1
        #     case 1| 3| 4| 5| 6| 7| 8| 9| 10| 11| 13| 15:
        #         y = y
        #     case _:
        #         print('匹配到其他通道')
        y = dat / m * 22
        formatted_num = '{:.6f}'.format(y)
        str1 = '\t'+ str(formatted_num)
        f2.write(str1)
        a = a + 2

    # f2.write('\n')





def match_example(item):
    pattern1 = b'\xEb\x90'
    n=0
    m = item.find(pattern1, n, 2176)
    f6.write(item[0:m])
    while n <2176:

        m = item.find(pattern1, n, 2176)
        m1 = item.find(pattern1, m+2, 2176)

        if m != -1:
            if m1 - m == 34:

                write(item[m+2:m+34],m1-m)

            elif m == 2176-34:
                write(item[m + 2:m + 34], 2176-m)


            else:
                None
            global t_temp1
            t_temp1 += 1 / fs
        else:
            break



        #     if m1 - m == 34:
        #
        #         write(item[m+2:m+34],m1-m)
        #         global t_temp1
        #         t_temp1 += 1 / fs


        # if m != -1:
        #     if m1!=-1:
        #         data_temp = item[m+2:m1]
        #
        #         # write(item[m+2:m+34],m1-m)
        #
        #
        #     else :
        #         data_temp = item[m + 2:2184]
        #         # write(item[m+2:m+34],2184-m)
        #     f6.write(data_temp)
        #     global t_temp1
        #     t_temp1 += 1 / fs
        # else:
        #     break
        n = m+2

def match_example_dat(item,eof):
    pattern1 = b'\xEb\x90'
    n=0
    while n <eof:

        m = item.find(pattern1, n, eof)
        m1 = item.find(pattern1, m+2, eof)
        m2 = item.find(pattern1, m1+2, eof)
        m3 = item.find(pattern1, m2+2, eof)

        if m != -1:
            if m1 - m == 34:

                write(item[m+2:m+34],m1-m)
                global t_temp1
                t_temp1 += 1 / fs
        else:
            break



            # if m1 - m == 34:
            #
            #     write(item[m+2:m+34],m1-m)
            #     global t_temp1
            #     t_temp1 += 1 / fs


        # if m != -1:
        #     if m1!=-1 :
        #         write(item[m + 2:m1], m1 - m)
        #         if m1-m != 34:
        #             global channel_cnt
        #             channel_cnt = 15
        #             write(item[m1 + 2:m2], m2 - m1)
        #             # write(item[m1 + 2:m2], m2 - m1)
        #             num = m3-m1-4
        #             while num <32:
        #                 write(item[m2+2:m3], m3-m2)
        #                 m2 = m3
        #                 m3 = item.find(pattern1, m3+2, eof)
        #                 num = num + m3 - m2 - 2
        #
        #
        #
        #         elif m1-m ==34:
        #             write(item[m1+2:m2], m2 - m1)
        #
        #     else:
        #         None
        #
        #
        #     # global t_temp1
        #     # t_temp1 += 1 / fs
        # else:
        #     break
        # if m2>0:
        #     n =m2
        # else:
        #     break
        n = m+2
        print('\r' +"解析中"+ "{:.2f}".format(n / 1000000) + '/' + "{:.2f}".format(eof1 / 1000000), end='', flush=True)




pattern = b'\x1a\xcf\xfc'
n = 0
while n <eof:
    m = data.find(pattern,n,eof)
    if m != -1:
        if data[m+3] == 16:
            match data[m+4]:
                case 17:
                    time0.append(t_temp1)
                    f0.write(data[m+8:m+2184])
                case 34:
                    time1.append(t_temp1)
                    f1.write(data[m+8:m+2184])
                case 51:
                    time3.append(t_temp1)
                    f3.write(data[m + 8:m + 2184])
                case 68:
                    time4.append(t_temp1)
                    f4.write(data[m + 8:m + 2184])
                case _:
                    print(data[m+7])
        elif data[m+3] == 29:
            # match_example(data[m+8:m+2184])
            f6.write(data[m+8:m+2184])
            # # print(data[m+2182:m+2184])
        f.write(data[m:m + 2184])
        # tongdao = data[m+7]
        # match_example(data[m+7:m+2183])
    else:
        break
    n=m+2184
    print('\r' + "分离中"+"{:.2f}".format(n / 1000000) + '/' + "{:.2f}".format(eof / 1000000), end='', flush=True)
# i =1
# for t in times:
#     f5.write(f"通道{i}开始时间：{t[1]}"+'\n')
#     i += 1


f6.close()
f6 = open("temp.dat","rb")
f6.seek(0,2)
eof1 = f6.tell()
f6.seek(0,0)
data1 = f6.read()
match_example_dat(data1,eof1)
# # plt.plot(list_length)
# # plt.show()
# f7.writelines('\n'.join(list_length))


for m in files:
    m.close()


print("helloworld")

# result = struct.unpack('format string', data)