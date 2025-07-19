import struct

import tkinter as tk
from base64 import encode
from tkinter import filedialog
import os
import math



def main():
    # 处理原始数据dat
    root = tk.Tk()
    root.withdraw()
    f_path = filedialog.askopenfilename()

    file = open(f_path, 'rb')
    file_name = f_path.split('.')[0]
    file.seek(0, 2)
    eof = file.tell()
    file.seek(0, 0)
    data = file.read()

    #

    class channelconfig:

        def __init__(self, fullscan, fs, len_bits, channelflag, en):
            self.fullscan = fullscan
            self.fs = fs
            self.len_bits = len_bits
            self.channelflag = channelflag
            self.en = en

        def fillconfig(self, file):
            self.file = file

    channel1 = channelconfig(fullscan=10, fs=10000, len_bits=16, channelflag=0, en=1)
    channel2 = channelconfig(fullscan=10, fs=10000, len_bits=16, channelflag=1, en=1)
    channel3 = channelconfig(fullscan=10, fs=10000, len_bits=16, channelflag=2, en=0)
    channel4 = channelconfig(fullscan=10, fs=10000, len_bits=16, channelflag=3, en=0)
    channel5 = channelconfig(fullscan=10, fs=10000, len_bits=16, channelflag=4, en=0)
    channel6 = channelconfig(fullscan=10, fs=10000, len_bits=16, channelflag=5, en=0)
    channel7 = channelconfig(fullscan=10, fs=10000, len_bits=16, channelflag=6, en=0)
    channel8 = channelconfig(fullscan=10, fs=10000, len_bits=16, channelflag=7, en=1)
    channel9 = channelconfig(fullscan=10, fs=10000, len_bits=16, channelflag=8, en=0)
    channel10 = channelconfig(fullscan=10, fs=10000, len_bits=16, channelflag=9, en=0)
    channel11 = channelconfig(fullscan=10, fs=10000, len_bits=16, channelflag=10, en=0)
    channel12 = channelconfig(fullscan=10, fs=10000, len_bits=16, channelflag=11, en=0)
    channel13 = channelconfig(fullscan=10, fs=10000, len_bits=16, channelflag=12, en=0)
    channel14 = channelconfig(fullscan=10, fs=10000, len_bits=16, channelflag=13, en=0)
    channel15 = channelconfig(fullscan=10, fs=10000, len_bits=16, channelflag=14, en=0)
    channel16 = channelconfig(fullscan=10, fs=10000, len_bits=16, channelflag=15, en=0)

    channellist = [channel1, channel2, channel3, channel4, channel5, channel6, channel7, channel8, channel9, channel10,
                   channel11, channel12, channel13, channel14, channel15, channel16]

    fillist = {}
    times = {}
    for i in range(16):
        if int(channellist[i].en) == 1:
            times[i + 1] = 0
            fillist[i + 1] = open( file_name +f"测试通道{i + 1}数据.txt", 'w+')
            fillist[i + 1].write('时间' + '\t' + f'通道{i + 1}' + '\n')
            channellist[i].fillconfig(file=fillist[i + 1])

    fillist[0] = open(file_name + "处理后结果.dat", "wb+")

    channellist_use = []
    flag_use = []
    m = 0
    for i in range(16):
        if int(channellist[i].en) == 1:
            channellist_use.append(channellist[i])
            flag_use.append(channellist[i].channelflag)

        else:
            pass

    print('\r' + "解析进度（MB):")

    def writedata(channel, cnt):
        data_step = math.ceil(channel.len_bits / 8)
        m = 2 ** (channel.len_bits - 1)
        i = 0
        k = cnt
        t_temp = times[channel.channelflag + 1]
        while i < 2176 / data_step:
            dat = data[k:k + data_step]
            dat = int.from_bytes(dat, byteorder='big', signed=True)
            # dat = dat /2**16*40-20
            t_temp = t_temp + 1
            y = dat / m * channel.fullscan

            str1 = '\t'.join([str(t_temp / channel.fs), str(y)]) + '\n'
            channel.file.write(str1)
            k = k + data_step
            i = i + 1
        times[channel.channelflag + 1] = t_temp

    pattern = b'\x1a\xcf\xfc\x1d'
    n = 0

    while n < eof:
        m = data.find(pattern, n, eof)
        if m != -1:
            # fillist[0].write(data[m:m + 2184])
            # k = channellist[2].channelflag
            # print(int(channellist[2].channelflag))
            if data[m + 7] in flag_use:
                use_seq = flag_use.index(data[m + 7])
                writedata(channellist_use[use_seq], m + 8)
            else:
                pass
        else:
            break
        n = m + 2184
        print('\r' + "{:.2f}".format(n / 1000000) + '/' + "{:.2f}".format(eof / 1000000), end='', flush=True)

    print('\r' + "Process  Done")

    for file in fillist:
        fillist[file].close()

    print('hello world')




if __name__ == "__main__":

    main()
