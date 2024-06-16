def exit():
    window.destroy()
 
def convert1():
    c = int(e1.get())
    f = ((c*9)/(5))+32
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,f)
    t1.config(state='disabled')

def convert2():
    f=int(e2.get())
    c=((f-32)/(1.8))
    t2.config(state='normal')
    t2.delete('1.0', tk.END)
    t2.insert(tk.END,c)
    t2.config(state='disabled')

import tkinter as tk
window = tk.Tk()
window.geometry("500x750")
window.config(bg="#33FFF1")
window.resizable(width=False,height=False)
window.title('Celsius <--> Fahrenheit Converter!')
 
h1 = tk.Label(window,text="Edu Skills project--2",font=("italic", 25,"bold"),fg="black",bg="#FF0000")
l1 = tk.Label(window,text="Celsius to Fahrenheit Converter",font=("Arial", 15),fg="#C83200",bg="#FF00FF")
l2= tk.Label(window,text="Enter temperature in Celsius: ",font=("Arial", 15,"bold"),fg="#C83200",bg="#33FFF1")
l3= tk.Label(window,text="Temperature in Fahrenheit is: ",font=("Arial", 15,"bold"),fg="#C83200",bg="#33FFF1")

b1 = tk.Label(window,text="Fahrenheit To Celsius Converter",font=("Arial", 15),fg="#C83200",bg="#FF00FF")
b2= tk.Label(window,text="Enter temperature in Fahrenheit: ",font=("Arial", 15,"bold"),fg="#C83200",bg="#33FFF1")
b3= tk.Label(window,text="Temperature in Celsius is: ",font=("Arial", 15,"bold"),fg="#C83200",bg="#33FFF1")

empty_h1 = tk.Label(window,bg="#33FFF1")
empty_l1 = tk.Label(window,bg="#33FFF1")
empty_l2 = tk.Label(window,bg="#33FFF1")
empty_l3 = tk.Label(window,bg="#33FFF1")
empty_l4 = tk.Label(window,bg="#33FFF1")
empty_b1 = tk.Label(window,bg="#33FFF1")
empty_b2 = tk.Label(window,bg="#33FFF1")
empty_b3 = tk.Label(window,bg="#33FFF1")
empty_b4 = tk.Label(window,bg="#33FFF1")
 
e1= tk.Entry(window,font=('Arial',10))

e2= tk.Entry(window,font=('Arial',10))


btn1 = tk.Button(window,text="Convert to Fahrenheit!",font=("Arial", 10),command=convert1)

btn3 = tk.Button(window,text="Convert to Celsius!",font=("Arial", 10),command=convert2)

btn2 = tk.Button(window,text="Exit application",font=("Arial", 10),command=exit)
 
t1=tk.Text(window,state="disabled",width=15,height=0)

t2=tk.Text(window,state="disabled",width=15,height=0)
 
h1.pack()
empty_h1.pack()
l1.pack()
empty_l3.pack()
l2.pack()
e1.pack()
empty_l1.pack()
btn1.pack()
empty_l4.pack()
l3.pack()
t1.pack()
empty_l2.pack()
b1.pack()
empty_b3.pack()
b2.pack()
e2.pack()
empty_b1.pack()
btn3.pack()
empty_b4.pack()
b3.pack()
t2.pack()
empty_b2.pack()
btn2.pack()
 
window.mainloop()
