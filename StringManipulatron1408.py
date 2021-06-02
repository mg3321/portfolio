#This program will ask the user to input 3 separate strings
#There are 3 functions to perform on the strings:
#Point 1 concatenates all 3 strings and changes them to upper case
#Point 2 concatenates 2 of the strings and changes them to lower case
#Point 3 returns the total number of characters in all 3 strings
#The result of any will be displayed in a separate window 
#Python has built-in 'upper' and 'lower' functions, but I wanted to write my own

from tkinter import *

def upper(string):#My own function for changing text case
    newString = ''
    for letter in string:
        if letter not in lowers:#doesn't change capitals, 
            newString += letter#numbers and special characters
            continue
        for char in range(len(lowers)):#swaps characters by 
            if letter == lowers[char]:#referring to index postions
                newString += uppers[char]
                break
    return newString

def lower(string):#Opposite of upper function
    newString = ''
    for letter in string:
        if letter not in uppers:
            newString += letter
            continue
        for char in range(len(uppers)):
            if letter == uppers[char]:
                newString += lowers[char]
                break
    return newString

def point1():#Concats and uppers all 3 strings
    newString = ''
    for i in range(3):
        newString += widgets[1][i].get()
    showResult(widgets[2][0], upper(newString))
    
def point2():#concats and lowers last and first strings
    newString = widgets[1][2].get() + widgets[1][0].get()
    showResult(widgets[2][1], lower(newString))

def point3():#Total number of chars in all 3 strings
    newString = ''
    for i in range(3):
        newString += widgets[1][i].get()
    result = ("There are " + str(len(newString)) +
              " characters in all 3 strings.")
    showResult(widgets[2][2], result)
    
def showResult(title, result):#To display result
    resultWindow = Tk()#Set up window
    resultWindow.geometry('300x250')
    resultWindow.title(title)
    scroll = Scrollbar(resultWindow)#Makes window scrollable
    messageField = Text(resultWindow)
    scroll.pack(side=RIGHT, fill=Y)
    messageField.pack(side=LEFT, fill=Y)
    scroll.config(command=messageField.yview)
    messageField.config(yscrollcommand=scroll.set)
    messageField.insert(END, result)#Display result

#Lists for functions and windows
lowers = 'abcdefghijklmnopqrstuvwxyz'
uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
widgets = [["String P:","String Q:","String R:"],["EntryP","EntryQ","EntryR"],
           ["Point 1","Point 2","Point 3"],[point1,point2,point3]]
#Main window
root = Tk()
root.title('Do Pythons Have Shells?')
for i in range(len(widgets[0])):#Places up widgets
     widgets[0][i] = Label(root, text=widgets[0][i]).grid(row=i,column=0)
     widgets[1][i] = Entry(root)#Had to be done on 2 lines to avoid TypeError
     widgets[1][i].grid(row=i,column=1)
     widgets[3][i] = Button(root, text=widgets[2][i],
                           command=widgets[3][i],
                            relief=RAISED, bd=5).grid(row=3, column=i)


root.mainloop()
