import tkinter as tk
from base64 import encode, decode
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()
f_path = filedialog.askopenfilename()
file = open(f_path, 'r')
file_name =f_path.split('.')[0]
f1 = open(file_name+"处理后结果1.txt", "w+")
f2 = open(file_name+"处理后结果2.txt", "w+")
f3 = open(file_name+"有效数据.txt", "w+")
lines_num = 0
with open(f_path, 'r') as f:
    for line in f.readlines():
        if lines_num <= 44250:
            # f1.write(line)
            f3.write(line)

        # elif 3300000<lines_num < 3440000:
        else:
            # f3.write(line)
            None
        lines_num += 1
f1.close()
f2.close()
f3.close()
print("文本行数"+str(lines_num))


