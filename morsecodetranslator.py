from tkinter import CENTER
from types import prepare_class
from typing import Text
import customtkinter as ctk

# · − 
morse_dic = {'a': '.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....',
'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-',
'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
'0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...',
'8':'---..', '9':'----.', '!':'-.-.--', '.':'.-.-.-', '(':'-.--.', ')':'-.--.-', '-':'-....-',
'+':'.-.-.', '=':'-...-', '@':'.--.-.', '&':'.-...', '?':'..--..', ',':'--..--', '\'':'.----.',
'\"':'.-..-.', ':':'---...'}
                    
def toMorse(input, outputBox):
  output = ''
  string = input.lower()
  for char in string:
     if char == ' ':
        output += '/'
     elif char == '\n':
       pass
     else:
      output += str(morse_dic[char]) + ' '
  outputBox.delete('0.0', 'end')
  outputBox.insert("0.0", str(output))
  #with open("copyfromhere.txt", 'a') as f:
    #f.write(output+'\n')

def toEnglish(input, outputBox):
  def toletter(x):
    morse = ''
    dictuple = morse_dic.items()
    for pair in dictuple:
      if x == pair[1]:
        morse += pair[0]
    return morse
  output = ''
  morse = input.lower().split(' ')
  for code in morse:
    for char in code:
      if char == '/':
        code = code.replace('/', '')
        output += ' '
    output += str.upper(toletter(code))
  outputBox.delete('0.0', 'end')
  outputBox.insert("0.0", output)
  #with open("copyfromhere.txt", 'a') as f:
    #f.write(output+'\n')

root = ctk.CTk()
root.title("Rod & Ish's Morse Code Translator")
root.geometry("500x400")
ctk.set_appearance_mode("dark")
root.grid_columnconfigure((0, 1, 2,), weight=1)
root.grid_rowconfigure((0,1,2,3,4), weight=1)
    
def homeScreen():
  
  title = ctk.CTkLabel(root, text='Morse Code Translator', fg_color = 'transparent', font=('Bodoni', 20))
  title.grid(row=1, column=1)
  greeting = ctk.CTkLabel(root, text='Welcome to the Morse Code Translator! \nClick start to get started!', fg_color ='transparent', font=('Bodoni', 15))
  greeting.grid(row=2, column=1)
  
  def onStart():
    for widgets in root.winfo_children():
      widgets.destroy()
    translateScreen()
  startBtn = ctk.CTkButton(master=root, text='Start', command=onStart, width=100, height=20)
  startBtn.grid(row=3, column=1, pady=10)

def translateScreen():
  morseInput = ctk.CTkTextbox(root, width=210, height=50)
  morseInput.grid(row=0, column=0, sticky='se')
  morseInput.insert('0.0', "Put Morse Code Here")
  
  morseOutput = ctk.CTkTextbox(root, width=210, height=50)
  morseOutput.grid(row=1, column=0, sticky='e')

  engInput = ctk.CTkTextbox(root, width=210, height=50)
  engInput.grid(row=0, column=2, sticky='sw')
  engInput.insert('0.0', "Put English Text Here")

  engOutput = ctk.CTkTextbox(root, width=210, height=50)
  engOutput.grid(row=1, column=2, sticky='w')
  
  morseTrans = ctk.CTkButton(root, text='Translate to English', command=lambda: toEnglish(morseInput.get("0.0", "end"), morseOutput), width=210, height=20)
  morseTrans.grid(row=2, column=0, sticky='e')

  engTrans = ctk.CTkButton(root, text='Translate to Morse', command=lambda: toMorse(engInput.get("0.0", "end"), engOutput), width=210, height=20)
  engTrans.grid(row=2, column=2, sticky='w')

  def back():
    for widgets in root.winfo_children():
      widgets.destroy()
    homeScreen()
  backBtn = ctk.CTkButton(root, text='Back', command=back, width=100, height=20)
  backBtn.grid(row=3, column=0, columnspan=3, sticky='s')

homeScreen()
root.mainloop()