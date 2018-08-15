#!/usr/bin/env python
# -*- coding: utf-8 -*-

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                           
#      ~ PyCrunch 1.0 beta ~                            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#       CoDeD: bY KURO-CODE
#       DaTe: 25/12/2017
#       Dev: Python (TKinter)
#
#~~~~~~~~~~~ INFO ~~~~~~~~~~~~~~~~~~~
#
#    Simple wordlist generator
#    GUI (Graphical User Interface) 
#
#************************************

# Module tkinter
from Tkinter import * 
from tkMessageBox import *
import itertools
import string
import subprocess
import os
import time
import webbrowser

# Main «root»
root = Tk()
root.title('PyCrunch 1.0')

# Image
photo = PhotoImage(file="PyCrunch.png")

canvas = Canvas(root,width=250, height=75)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack(side=TOP, padx=1, pady=1)

# Title
l = LabelFrame(root, text="PyCrunch 2017", padx=20, pady=20)
l.pack(fill="both", expand="yes")




# Label info 
Label(l, text="Simple WordList geneator\nCoded By KURO-CODE").pack()

# Build wordlist
def GET():
   ch= chars.get()
   mn= value1.get()
   mx= value2.get()
   N_file='Wordlist.txt'
   ln=len(ch)
   TXT=[]

   file = open(N_file, 'a')
   for x in xrange(mn,mx+1):
	meta=ln**x
   	TXT.append(meta)
   	TXT_line=sum(TXT)

   	for xs in itertools.product(ch, repeat=x):
   		file.write(''.join(xs)+'\n')
   file.close()
   Finish()

# Finish & Exit
def Finish():
   print "[*] Finish!"
   showinfo('INFO', 'File Finish!')
   showinfo('Exit', 'Thanks for using PyCrunch!')
   sys.exit()
   
# Var
value = StringVar() 
value.set("Chars")
chars = Entry(root, textvariable=value, width=20)
chars.pack( padx=5, pady=5)

value1 = IntVar() 
value1.set("Min")
MIN = Entry(root, textvariable=value1, width=20)
MIN.pack( padx=5, pady=5)

value2 = IntVar() 
value2.set("Max")
MAX = Entry(root, textvariable=value2, width=20)
MAX.pack( padx=5, pady=5)

def callinfo():
     showinfo('INFO', 'PyCrunch 1.0 (WordList Generator)\t\nInterface: GUI\nDate: 25/12/2017\nDev: Python (TK)\nVer: 1.0 beta\nCoded by KURO-CODE\t')

def ABOUT():
   webbrowser.open('https://github.com/KURO-CODE?tab=repositories')	

def EXIT():
   showinfo('Closing', 'Thanks for using PyCrunch!')
   root.quit()

# frame 1
Frame1 = Frame(root, borderwidth=1, relief=GROOVE)

# button «OK "build wordlist"»
qb = Button(root, text='Ok', command=GET)
qb.pack(side=LEFT,padx=5, ipadx=15, pady=5)
# button «INFO "call INFO»
qb = Button(root, text='Info', command=callinfo)
qb.pack(side=LEFT, padx=5, ipadx=10, pady=5)
# button «ABOUT "call ABOUT"»
qb = Button(root, text='About', command=ABOUT)
qb.pack(side=LEFT, padx=5, ipadx=10, pady=5)
# button «EXIT "call EXIT"»
qb = Button(root, text='Exit', command=EXIT)
qb.pack(side=LEFT, padx=5, ipadx=10, pady=5)

Frame1.pack(side=LEFT, padx=0, pady=20)
# Run main «MAIN»
root.mainloop()
