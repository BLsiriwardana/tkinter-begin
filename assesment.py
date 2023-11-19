import tkinter as tk
import win32api
from win32api import GetSystemMetrics
from tkinter import ttk

#create window
root = tk.Tk()
screen_width = GetSystemMetrics(0)  #/screen_width = root.winfo_screenwidth()
screen_height = GetSystemMetrics(1) #screen_height = root.winfo_screenwidth()
window_width = 400
window_height = 500
x_position = (screen_width/2 ) - (window_width/2)
y_position = (screen_height/2) - (window_height/2)

#print(screen_height)
#print(screen_width)
root.geometry(f'{window_width}x{window_height}+{int(x_position)}+{int(y_position)}')
root.iconbitmap("Cal.ico")
root.title("calculator")
root.resizable(False,False)
#VARIABLE

#FUNCTION
text_1 = "+"
def plus():
    text_1 = "+"
    label_1.configure(text=text_1)
    #print("hi")
    num_1 = int(entry_1.get())
    num_2 = int(entry_2.get())
    label_2.configure(text=str(num_1)+text_1+str(num_2)+" = "+str(num_1+num_2))
def min():
    text_1 = "-"
    label_1.configure(text=text_1)
    #print("hi")
    num_1 = int(entry_1.get())
    num_2 = int(entry_2.get())
    label_2.configure(text=str(num_1)+text_1+str(num_2)+" = "+str(num_1-num_2))


    #print(str(num_1+num_2))
   
def mul():
    text_1 = "*"
    label_1.configure(text=text_1)
    #print("hi")
    num_1 = int(entry_1.get())
    num_2 = int(entry_2.get())
    label_2.configure(text=str(num_1)+text_1+str(num_2)+" = "+str(num_1*num_2))

def div():
    text_1 = "/"
    label_1.configure(text=text_1)
    #print("hi")
    num_1 = int(entry_1.get())
    num_2 = int(entry_2.get())
    label_2.configure(text=str(num_1)+text_1+str(num_2)+" = "+str(num_1/num_2))

def force():
    text_1 = "^"
    label_1.configure(text=text_1)
    #print("hi")
    num_1 = int(entry_1.get())
    num_2 = int(entry_2.get())
    
    
    if int(num_2) == 0:
           label_2.configure(text=str(num_1)+text_1+str(num_2)+" =  1")
           
    else :
          x = 1
          y = 1
          while x <= num_2:
              y=y*num_1
              x =  x + 1 
          label_2.configure(text=str(num_1)+text_1+str(num_2)+" =  "+str(y))
 
     


#WEIGET
entry_1 = ttk.Entry(root)
entry_1.grid(row=2, column=1,columnspan=2, pady=10)

label_1 = ttk.Label(root)
label_1.grid(row=2,column=3, pady=10)
 

entry_2 = ttk.Entry(root)
entry_2.grid(row=2,column=4, columnspan=2, pady=10)

plus = ttk.Button(root, text="+", command=plus)
plus.grid(row=3, column=1, pady=8,)

min = ttk.Button(root, text="-",command=min)
min.grid(row=3, column=2, pady=8)

mul = ttk.Button(root, text="*", command=mul)
mul.grid(row=3, column=3, pady=8)

div = ttk.Button(root, text="/", command=div)
div.grid(row=3, column=4, pady=8)

force = ttk.Button(root, text="/" , command=force)
force.grid(row=3, column=5, pady=8)

label_2 = ttk.Label(root)
label_2.grid(row=4, column=3, pady=5)

root.mainloop()