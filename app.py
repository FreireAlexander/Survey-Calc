from tkinter import *
from tkinter import ttk

# Setting Main Windows
root = Tk()
root.title("Icons and Images")
icon = PhotoImage(file='icons/icon.png')
root.tk.call('wm', 'iconphoto', root._w, icon)
root.configure(bg='white')
## Style for buttons
BT1 = ttk.Style()
BT1.configure('S1.TButton', background='#dae9fd', activebackground='red', 
                relief='raised', anchor='w',
                foreground='black', font=('Ubuntu', 40 ))
## Styles for Labels
LB1 = ttk.Style()
LB1.configure('L1.Label',background='white', justify='left')

## Main windows with principal Options
Main_Title = ttk.Label(root, text="Survey Calc", style='L1.Label',
                        font="Ubuntu 60 bold").grid(row=0, column=0, pady=20, padx=20, sticky='w')

Main_Subtitle = ttk.Label(root, text="What Would you like to calculate?", style='L1.Label',
                        font="Ubuntu 40 bold").grid(row=1, column=0, pady=20, padx=40, sticky='w')
# Button for option Angles from Coordinates
options = LabelFrame(root, text="Options", font=('Ubuntu', 32 ), background='white', bd=4)
options.grid(row=2, column=0, padx=10, pady=20)
Main_Button_1 = ttk.Button(options, text=' Angles from Coordinates', command='', style='S1.TButton')
Main_Button_1.grid(row=2, column=0, pady=20, padx=100, sticky='we')

# Button for option Whole Circle Bearing
Main_Button_2 = ttk.Button(options, text=' Whole Circle Bearing or Bearing', command='', style='S1.TButton'
                            ).grid(row=3, column=0, pady=20, padx=100, sticky='we')
# Button for option Coordinates
Main_Button_3 = ttk.Button(options, text=' Coordinates', command='', style='S1.TButton'
                            ).grid(row=4, column=0, pady=20, padx=100, sticky='we')

## Main Loop for the main windows
root.mainloop()