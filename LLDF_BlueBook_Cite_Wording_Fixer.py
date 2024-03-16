<<<<<<< HEAD

=======
print("JohnnyTech BlueBook Cite Abbreviation Fixer - Running imports...")
>>>>>>> 5e76d0aec51cd16a7fe6ec2d387e5b16c11a0837
import csv
import tkinter as tk
from tkinter import ttk
import urllib
<<<<<<< HEAD
def readconfig():
    reader = csv.DictReader(open('BlueBook.csv'))
    for row in reader:
        return
=======
import time
print("Definiiing varibles...")
def readconfig():
    reader = csv.DictReader(open('BlueBook.csv'))
    for row in reader:
        return row

    
print("Reading configuration table...")
config = readconfig()
print("Initalizing GUI...")
window = tk.Tk()
window.title("JohnnyTech BlueBook Cite Abbreviation Fixer")
window.geometry("524x856")
print("Initalizing GUI theme...")
window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "dark")
print("Initalizing GUI elements...")
header = ttk.Label(window,text="JohnnyTech BlueBook Cite Abbreviation Fixer\nEnter your old cite:")
brokencite = tk.Text(window)
cflbl = ttk.Label(window,text="Your fixed cite is here:")
fxc = tk.Text(window)
print("Definiiing varibles...")
def fixcite():
    print("Making varribles global...")
    global config
    print("Getting cite from input box...")
    cite = brokencite.get("1.0","end-1c")
    print("Defineing varribles...")
    def replace_from_config(config, input_string):
        print("Going through items...")
        for key, value in config.items():
            print("Running search and replace...")
            input_string = input_string.replace(key, value)
        return input_string    
    fixedcite = replace_from_config(config,cite)
    fxc.insert("1.0",fixedcite)
def setcharlimit(value):
    my_str=brokencite.get('1.0','end-1c')
    breaks=my_str.count('\n') 
    char_numbers=len(my_str)-breaks  
    if(char_numbers > 20):
        brokencite.delete('end-2c')

    
    

    
    
    
    
print("Initalizing GUI elements...")   
fixbutton = ttk.Button(window,text="Fix this cite",command=lambda: fixcite(), style='Accent.TButton')
print("Applying GUI elements...")
header.pack()
brokencite.pack()
fixbutton.pack()
cflbl.pack()
fxc.pack()


>>>>>>> 5e76d0aec51cd16a7fe6ec2d387e5b16c11a0837

config = readconfig()
window = tk.Tk()

header = ttk.Label(window,text="JohnnyTech LLDF BlueBook Cite Wording Fixer\nEnter unabbreviated cite below:")
brokencite = tk.Text(window)
def fixcite(cite):
    global config,output
    
    def replace_from_config(config, cite):
        try:
            for key, value in config.items():
                input_string = input_string.replace(key, value)
            return input_string
        except:
            pass
    try:
        fixedcite = replace_from_config(config,cite)

    except:
        pass
    try:
        output = fixedcite
    except:
        print("ERROR: THE SYSTEM CANNOT IMPORT THE FIXED CONTENT")
    

def fxc():
    fixcite(brokencite.get(1.0,"end"))
    if output == None:
        print("ERROR: INTERNAL DATA PROCESESING ERROR!\nPLEASE CONTACT JOHNNYTECH.")
    else:
        print("output:\n",output)
    
    
fixbutton = ttk.Button(window,text="Fix this cite",command= lambda:fxc())
header.pack()
brokencite.pack()
fixbutton.pack()
window.mainloop()