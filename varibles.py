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
root.title("variables")
root.iconbitmap("correct.ico")
root.resizable(False,False)

#weiget
value_text = tk.StringVar(value="") 
label_1 = ttk.Label(root, textvariable=value_text)
label_1.pack()

entry_1 = ttk.Entry(root, textvariable=value_text)
entry_1.pack()

button_1 = ttk.Button(root, text="click to print", command=lambda:print(entry_1.get()))
button_1.pack()

root.mainloop()