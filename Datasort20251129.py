import struct

import tkinter as tk
from base64 import encode
import multiprocessing
from tkinter import filedialog
import os
import cProfile
from threading import Thread
from multiprocessing import  Pool
import time
start_time = time.time()






fullscale = 5
dvidide = 5.5
datefull_16 = 2**15
datefull_32 = 2**31
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
t_temp = [0,0,0,0,0,0,0,0]


file = open(f_path, 'rb')
file_name =f_path.split('.')[0]
file.seek(0,2)
eof = file.tell()
file.seek(0,0)
data = file.read()
f = open(file_name+"处理后结果.dat", "wb+")
# f0 = open("通道1数据.txt",'w+',encoding='utf-8')
# f1 = open("通道2数据.txt",'w+',encoding='utf-8')
# f2 = open("通道3数据.txt",'w+',encoding='utf-8')
# f3 = open("通道4数据.txt",'w+',encoding='utf-8')
# f4 = open("通道5数据.txt",'w+',encoding='utf-8')
# f5 = open("通道6数据.txt",'w+',encoding='utf-8')
# f6 = open("通道7数据.txt",'w+',encoding='utf-8')
# f7 = open("通道8数据.txt",'w+',encoding='utf-8')

f8 = open("通道1数据.dat", "wb+")
f9 = open("通道2数据.dat", "wb+")
f10 = open("通道3数据.dat", "wb+")
f11 = open("通道4数据.dat", "wb+")
f12 = open("通道5数据.dat", "wb+")
f13 = open("通道6数据.dat", "wb+")
f14 = open("通道7数据.dat", "wb+")
f15 = open("通道8数据.dat", "wb+")
# files = [f,f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15]
files = [f,f8,f9,f10,f11,f12,f13,f14,f15]
filelist1 = ["通道1数据","通道2数据","通道3数据","通道4数据","通道5数据","通道6数据","通道7数据","通道8数据"]


fs = 100000


def write16(item,k,t_temp):
    i = 0
    str1 = ""


    while i <= 1087:
        dat = data[k:k+2]
        dat = int.from_bytes(dat, byteorder='big',signed=True)
        # dat = dat /2**16*40-20
        t_temp = t_temp + 1
        y = dat / datefull_16 * fullscale
        y= format(y,'.4f')

        str1 = str1+'\t'.join([str(t_temp/fs), str(y)]) + '\n'
        # item.write(str1)
        k = k+2
        i = i+1
    item.write(str1)
    return t_temp


def write32(item,k,t_temp):
    i = 0
    while i <= 543:
        dat_b = data[k:k+3]
        dat = int.from_bytes(dat_b, byteorder='big',signed=True)

        t_temp = t_temp + 1
        y = dat/datefull_32*fullscale

        str1 = '\t'.join([str(t_temp/fs), str(y)])+'\n'
        # item.write(str1)

        k = k+4
        i = i+1
    return t_temp

def translate(file_d):
    file_dat = open(file_d+".dat", 'rb')
    file_txt = open(file_d+".txt",'w+')
    # file = file_dat
    file_dat.seek(0, 2)
    eof = file_dat.tell()
    file_dat.seek(0, 0)
    data = file_dat.read()
    k = 0
    t_temp = 0
    while k <= eof:
        dat_b = data[k:k+1]
        dat = int.from_bytes(dat_b, byteorder='big',signed=True)

        t_temp = t_temp + 1
        y = dat/datefull_16*fullscale
        y = format(y, '.4f')
        str1 = '\t'.join([str(t_temp/fs), str(y)])+'\n'
        file_txt.write(str1)

        k = k+2

    file_dat.close()
    file_txt.close()
    print(file_d+".dat finished")
    # return "helloworld"





def match_example(item,m1):
    match item:
        case 0:
            f8.write(data[m1:m + 2176])
        case 1:
            f9.write(data[m1:m + 2176])
        case 2:
            f10.write(data[m1:m + 2176])
        case 3:
            f11.write(data[m1:m + 2176])
        case 4:
            f12.write(data[m1:m + 2176])
        case 5:
            f13.write(data[m1:m + 2176])
        case 6:
            f14.write(data[m1:m + 2176])
        case 7:
            f15.write(data[m1:m + 2176])
        case _:
            None
            # print("匹配到其他情况")



if __name__ == '__main__':
    pattern = b'\x1a\xcf\xfc\x1d'
    n = 0
    print('\r' + "解析进度（MB):")
    while n < eof:
        m = data.find(pattern, n, eof)
        if m != -1:

            match_example(data[m + 7], m + 8)

        else:
            break
        n = m + 2184
        print('\r' + "{:.2f}".format(n / 1000000) + '/' + "{:.2f}".format(eof / 1000000), end='', flush=True)
    # with Pool(4) as p:
    #     print(p.map(translate, filelist1))
    #
    # print(time.time() - start_time)

    # p1 = Process(target=translate,args= (f8.name, f0.name, ) )
    # # # thread2 = Process(target=translate, args=(f9, f1, ) )
    # # # thread3 = Process(target=translate, args=(f10, f2, ) )
    # # # thread4 = Process(target=translate, args=(f11, f3, ) )
    # # # thread5 = Process(target=translate, args=(f12, f4, ) )
    # # # thread6 = Process(target=translate, args=(f13, f5, ) )
    # # # thread7 = Process(target=translate, args=(f14, f6, ) )
    # # # thread8 = Process(target=translate, args=(f15, f7, ) )
    # # # threads = [thread1,thread2,thread3,thread4,thread5,thread6]
    # # # for t in threads:
    # # #     t.start()
    # # #
    # # # for t in threads:
    # # #     t.join()
    # p1.start()
    #
    # p1.join()

    while file in files:
        file.close()

    print('\r' + "Process  Done")



# result = struct.unpack('format string', data)