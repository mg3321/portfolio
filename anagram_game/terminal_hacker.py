##This is a terminal hacker game using anagrams.
##The user gets 5 attempts to guess the password from a clue.
##If the user fails after 5 attempts, the game is lost.
##Passwords are chosen and jumbled from a list in a separate file.

import random, passwords
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

def jumble(): #Chooses password and makes anagram clue
    global word, attempts

    update()
    wordsLen = len(passwords.Passwords) #Get range of passwords
    r = random.randrange(0,wordsLen)
    word = passwords.Passwords[r] #Choose random password from range
    wordlen = len(word)
    counter = wordlen
    anagramArray = [None] * wordlen #Empty list for assembling anagram
    anagram = ""

    while counter>0:
        r2 = random.randrange(0,wordlen) #Chooses character from word
        if anagramArray[r2] == None: #Puts character into empty slot
            anagramArray[r2] = word[counter-1]
            counter -= 1

    for i in anagramArray: #Repackage list as a string
        anagram += i
    
    anagramLabel['text'] = anagram #Display Clue

def answer(event): #Gets answer from user
    global word, attempts

    feedbackLabel['text'] = ("Awaiting Input...")
    answer = answerField.get()

    if answer == word: # If answer is correct
        if messagebox.askyesno('Access Granted!', #replay option
                               'Would you like to play again?'):
            answerField.delete(0,END)
            attempts = 5 #Reset attempts remaining
            jumble() #Play again
        else: #User quits
            messagebox.showinfo('Goodbye',
                                'Thank you for playing!')
            root.destroy() #Terminate Program

    else: #Wrong answer
        feedbackLabel['text'] = ("Access Denied") 
        answerField.delete(0,END)
        attempts -= 1
        update()
        if attempts < 1: #Too many attempts, game closes
            messagebox.showerror('Error', 'Account Locked. Please Contact IT'
                                 ' services for some "help"')
            root.destroy() #Terminate Program

    
def update(): #Updates attempts remaining label
    attemptsLabel['text'] = attempts


root = Tk() #Set up window
root.geometry("420x200")
root.title('Terminal Hacker')
root.config(bg='black')

clueLabel = Label(root, text='Clue:', bg='black', fg='white').pack()

anagramLabel = Label(root, bg='black', fg='white')
anagramLabel.pack()

answerField = Entry(root, bg='black', fg='white')
answerField.bind('<Return>', answer)
answerField.focus_set()
answerField.pack()

feedbackLabel = Label(root, bg='black', fg='white')
feedbackLabel.pack()

attemptsRemaining = Label(root, bg='black', fg='white',
                          text='Attempts Remaining:')
attemptsRemaining.pack()

attemptsLabel = Label(root, bg='black', fg='white')
attemptsLabel.pack()

attempts = 5 #Initialise attempts

jumble() #Starts game

root.mainloop()






