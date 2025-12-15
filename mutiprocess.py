from ctypes import create_string_buffer
from multiprocessing import Pool

import time
import itertools

from pandas.io.formats.style import buffering_args

start_time = time.time()
f8 = open("通道1数据.dat", "rb")
f0 = open("通道1数据.txt",'w+',encoding='utf-8')
datefull_16 = 2**15
fullscale = 5
fs= 100000

filelist1 = ["通道1数据","通道2数据","通道3数据","通道4数据","通道5数据","通道6数据","通道7数据","通道8数据"]
buffer = create_string_buffer(2048)
# list1 = []





def translate(file_d):
    file_dat = open(file_d+".dat", 'rb')
    file_txt = open(file_d+".txt",'w')
    # file = file_dat
    file_dat.seek(0, 2)
    eof = file_dat.tell()
    file_dat.seek(0, 0)
    data = file_dat.read()
    k = 0
    t_temp = 0
    list1 = []

    # i=0
    # str1=""
    while k < eof:
        m=0
        while m <= 100:
            dat_b = data[k:k + 2]
            dat = int.from_bytes(dat_b, byteorder='big', signed=True)

            t_temp = t_temp + 1
            y = dat / datefull_16 * fullscale
            y = format(y, '.4f')
            str1 = '\t'.join([str(t_temp / fs), str(y)]) + '\n'
            list1.append(str1)
            # file_txt.write(str1)

            k = k + 2
            m = m+1
            # if i<=1000:
            #     str1 = str1 +'\t'.join([str(t_temp/fs), str(y)])+'\n'
            #     i=i+1
            # else:
            #     file_txt.write(str1)
            #     str1 = ""
            #     i=0



        file_txt.writelines(list1)
        list1 = []
    file_dat.close()
    file_txt.close()
    print(file_d+".dat finished")
    # return "helloworld"



if __name__ == '__main__':
    with Pool(4) as p:
        print(p.map(translate,filelist1))

    print(time.time()-start_time)
    # translate("通道7数据")


    # p1 = Process(target=translate, args=(f8.name, f0.name,))
    # p1.start()
    # p1.join()