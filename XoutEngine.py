import pyttsx3
import os
engine = pyttsx3.init()
rate = engine.getProperty('rate')

engine.setProperty('rate', 125)            # for speak speed & its rate

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)  #for woman 1 & for men 0

Login = os.getlogin()

WriteMe = []                                #for show your live writing 
#_________Main program______________
def Ques():# Question about your choise for listen to information
    B = open('Ques.csv')
    UserID = []
    UserID.append(Login)
    engine.say('Hi' + UserID[0] + 'Welcome to XoutEngine')
    engine.runAndWait()
    for Z in B:
        engine.say(Z)
        engine.runAndWait()
def info():# the information
    UserID = []
    UserID.append(Login)
    engine.say('Hi ' + UserID[0] + 'Again')
    engine.runAndWait()
    A = open('Data.csv')
    for E in A:
        engine.say(E)
        engine.runAndWait()
Ques()
Input = int(input('Enter your number: ')) 
if Input == 1:
    info()

try:

    def inter():# file Reader 
        for items in os.listdir():
            print(items)
        engine.say('Enter your item name at below list with its format')
        engine.runAndWait()
        intr = str(input('Enter your item name: ')) 
        intl = []
        intl.append(intr)
        OP = open(intr)
        for filey in OP:
            engine.say(filey)
            engine.runAndWait()   
except:
    print('No such file in directory')
try:
    def write():# live Reader
        WRM = str(input('WriteMe: '))
        engine.say(WRM)
        engine.runAndWait()
        engine.save_to_file(WRM, WriteMe)
except:
    print('Only string!')

INPUT = int(input('Enter your Number: '))

if INPUT == 1:
    write()
elif INPUT == 2:
    inter()    