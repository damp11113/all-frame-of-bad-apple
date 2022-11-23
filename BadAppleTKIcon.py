from damp11113 import sort_files
import time
from damp11113.file import allfiles
import tkinter

root = tkinter.Tk()

root.title('Bad Apple On TK Icon')

T1 = tkinter.Text(root)
T1.tag_configure("center", justify='center')
T1.insert("1.0", "Lock at window icon")
T1.tag_add("center", "1.0", "end")
T1.pack()

badapplefile = sort_files(allfiles(r'badappleframe'))

for i in badapplefile:
    root.title(f'Bad Apple On TK Icon [{i}/{len(badapplefile)}]')
    p1 = tkinter.PhotoImage(file=f'badappleframe\\{i}')
    root.iconphoto(False, p1)
    time.sleep(0.029)
    root.update()
