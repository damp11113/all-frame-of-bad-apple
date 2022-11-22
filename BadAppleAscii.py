import serial
from damp11113.media import im2ascii
from damp11113 import sort_files
from damp11113.cmd import clear, size, title
import time
from damp11113.file import allfiles

rx = 120
ry = 70

badapplefile = sort_files(allfiles(r'C:\Users\sansw\Documents\pythonProject\badappleframe'))
#size(rx, ry)

for i in badapplefile:
    title(f'frame {i}/{len(badapplefile)}')
    print(im2ascii(f'C:\\Users\\sansw\\Documents\\pythonProject\\badappleframe\\{i}', width=rx, height=ry))
    time.sleep(0.029)
    #clear()