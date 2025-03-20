import struct

import tkinter as tk
from base64 import encode
from tkinter import filedialog
import os
root = tk.Tk()
root.withdraw()
f_path = filedialog.askopenfilename()


file = open(f_path, 'rb')
file_name =f_path.split('.')[0]
data = file.read()
f = open(file_name+"文件复制.dat", "wb+")




for i in range(0,6):
    f.write(data)


f.close()


print("helloworld")

# result = struct.unpack('format string', data)