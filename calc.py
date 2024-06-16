# import everything from tkinter module 
from tkinter import *
import tkinter.font as font
expression = "" 

# in the text entry box 
def press(num): 
	global expression
	
	expression = expression + str(num) 

	# update the expression by using set method 
	equation.set(expression) 


# Function to evaluate the final expression 
def equalpress(): 
	# which may generate the error 
	try: 

		global expression 

		# eval function evaluate the expression 
		# and str function convert the result 
		# into string 
		total = str(eval(expression)) 

		equation.set(total) 

		# initialize the expression variable 
		# by empty string 
		expression = "" 
	except: 

		equation.set(" error ") 
		expression = "" 


# Function to clear the contents 
# of text entry box 
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 


# Driver code 
if __name__ == "__main__": 
	# create a GUI window 
	gui = Tk() 

	# set the background colour of GUI window 
	gui.configure(background="light green") 

	# set the title of GUI window 
	gui.title("Simple Calculator") 

	# set the configuration of GUI window 
	gui.geometry("600x600")
	
	# we create an instance of this class 
	equation = StringVar() 

	# create the text entry box for 
	# showing the expression . 
	expression_field = Entry(gui, textvariable=equation) 

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure .
	expression_field.config(font=("Courier", 24))
	expression_field.grid(columnspan=7, ipadx=17)

	# create a Buttons and place at a particular 
	# location inside the root window . 
	# when user press the button, the command or 
	# function affiliated to that button is executed .
	f = font.Font(family='Times New Roman',weight="bold")

	
	button1 = Button(gui, text=' 1 ', fg='white', bg='#38B6E8',relief=RAISED, 
					command=lambda: press(1), height=4, width=10)

	button1['font'] = f
	
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='white', bg='#38B6E8',relief=RAISED, 
					command=lambda: press(2), height=4, width=10) 
	button2.grid(row=2, column=1) 

	button2['font'] = f

	button3 = Button(gui, text=' 3 ', fg='white', bg='#38B6E8',relief=RAISED, 
					command=lambda: press(3), height=4, width=10) 
	button3.grid(row=2, column=2)
	
	button3['font'] = f

	button4 = Button(gui, text=' 4 ', fg='white', bg='#38B6E8',relief=RAISED, 
					command=lambda: press(4), height=4, width=10) 
	button4.grid(row=3, column=0)

	button4['font'] = f

	button5 = Button(gui, text=' 5 ', fg='white', bg='#38B6E8',relief=RAISED, 
					command=lambda: press(5), height=4, width=10) 
	button5.grid(row=3, column=1)

	button5['font'] = f

	button6 = Button(gui, text=' 6 ', fg='white', bg='#38B6E8',relief=RAISED,
					command=lambda: press(6), height=4, width=10) 
	button6.grid(row=3, column=2)

	button6['font'] = f

	button7 = Button(gui, text=' 7 ', fg='white', bg='#38B6E8',relief=RAISED, 
					command=lambda: press(7), height=4, width=10) 
	button7.grid(row=4, column=0)

	button7['font'] = f

	button8 = Button(gui, text=' 8 ', fg='white', bg='#38B6E8',relief=RAISED, 
					command=lambda: press(8), height=4, width=10) 
	button8.grid(row=4, column=1)

	button8['font'] = f

	button9 = Button(gui, text=' 9 ', fg='white', bg='#38B6E8',relief=RAISED, 
					command=lambda: press(9), height=4, width=10) 
	button9.grid(row=4, column=2)

	button9['font'] = f

	button0 = Button(gui, text=' 0 ', fg='white', bg='#38B6E8',relief=RAISED, 
					command=lambda: press(0), height=4, width=10) 
	button0.grid(row=5, column=0)

	button0['font'] = f

	plus = Button(gui, text=' + ', fg='white', bg='#38B6E8',relief=RAISED, 
				command=lambda: press("+"), height=4, width=10) 
	plus.grid(row=2, column=3)

	plus['font'] = f

	minus = Button(gui, text=' - ', fg='white', bg='#38B6E8',relief=RAISED, 
				command=lambda: press("-"), height=4, width=10) 
	minus.grid(row=3, column=3)

	minus['font'] = f

	multiply = Button(gui, text=' * ', fg='white', bg='#38B6E8',relief=RAISED, 
					command=lambda: press("*"), height=4, width=10) 
	multiply.grid(row=4, column=3)

	multiply['font'] = f

	divide = Button(gui, text=' / ', fg='white', bg='#38B6E8',relief=RAISED, 
					command=lambda: press("/"), height=4, width=10) 
	divide.grid(row=5, column=3)

	divide['font'] = f

	equal = Button(gui, text=' = ', fg='white', bg='#38B6E8',relief=RAISED,
                       command=equalpress, height=4, width=10) 
	equal.grid(row=5, column=2)

	equal['font'] = f

	clear = Button(gui, text='Clear', fg='white', bg='#38B6E8',relief=RAISED, 
				command=clear, height=4, width=10) 
	clear.grid(row=6,column=0)

	clear['font'] = f

	Decimal= Button(gui, text='.', fg='white', bg='#38B6E8',relief=RAISED, 
					command=lambda: press('.'), height=4, width=10) 
	Decimal.grid(row=5, column=1)

	Decimal['font'] = f
	# start the GUI 
	gui.mainloop() 
