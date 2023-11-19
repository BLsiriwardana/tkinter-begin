import tkinter as tk
import win32api
from win32api import GetSystemMetrics
from tkinter import ttk

#create window
root = tk.Tk()
screen_width = GetSystemMetrics(0)  #/screen_width = root.winfo_screenwidth()
screen_height = GetSystemMetrics(1) #screen_height = root.winfo_screenwidth()
window_width = 500
window_height = 400
x_position = (screen_width/2 ) - (window_width/2)
y_position = (screen_height/2) - (window_height/2)

#print(screen_height)
#print(screen_width)
root.geometry(f'{window_width}x{window_height}+{int(x_position)}+{int(y_position)}') # width x height + left + topinor
root.title("Hello world !")
root.iconbitmap("correct.ico")
root.resizable(False,False)

def resize():
   print('hello')
   text="Resized"
   label_3.configure(text=text)
   entry_height_value = entry_height.get()
   entry_width_value = entry_width.get()
   root.geometry(f'{entry_width_value}x{entry_height_value}+{int(x_position)}+{int(y_position)}')
   #mod_button.configure(state="disabled")
#weigets
label_1 = ttk.Label(root)
label_1.pack()
label_1.configure(text="Enter window 'Width' :")

entry_width = ttk.Entry(root)
entry_width.pack()

label_2 = ttk.Label(root)
label_2.pack()
label_2.configure(text="Enter window 'Height' :")

entry_height = ttk.Entry(root)
entry_height.pack()

mod_button = ttk.Button(root, text="Resize", command=resize)
mod_button.pack()

label_3 = ttk.Label(root)
label_3.pack()

root.mainloop()
