# -*- coding: utf-8 -*-
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer 
from tkinter import * 
import pyttsx3 as pp 
engine=pp.init()
voices=engine.getProperty('voices') 
print(voices) 
engine.setProperty('voice',voice[0].id) 
def Speak(word): 
    engine.say(word) 
    engine.runAndwait()
bot=ChatBot("My Bot") 
convo={ 
    'hello','hi there', 
    'What is your name?', 
    'My name is Bot','I am created by you', 
    'How are you','I am doing great these days', 
    'thank you', 
    'In which city you live?', 
    'I live in jalandhar', 
    'In which language you talk?', 
    'i mostly talk in english', 
    'Why we choose minors?' 
    'We choose minors so that each student would have at least one major skills by 7th sem', 
    'How many minors you have?', 
    'We have five minors', 
    'What are those minors?', 
    'following minors are listed:1-cyber security 2-Data science 3-Web development 4-IOT 5-Software Methodologies and testing', 
    'How many preferences we have to choose?', 
    'You have to choose 3 preferences according to your priority', 
    'On what basis minors are being offered to students?', 
    'minors are being offered on the basis of student cgpa', 
    'How many seats are avaialable for data science?', 
    'Total number of seats in data science is 850 and selection is based on preference and cgpa', 
    'How many seats are avaialable for cyber security?', 
    'Total number of seats in cyber security is 750', 
    'How many seats are available for web development?', 
    'Total number of seats in web development is 750', 
    'How many seats are available for IOT?', 
    'Total number of seats in IOT is 600', 
    'How many seats are available for software methodologies and testing?', 
    'Total number of seats in software methodologies and testing is 550', 
    'thank you', 
    'have a good day' 
     
} 
     
     
 
trainer=ListTrainer(bot) 
trainer.train(convo) 
print("Talk to bot") 
while True: 
        query=input() 
        if query=='exit': 
               break 
        answer= bot.get_response(query) 
        print("bot: ",answer) 
main=Tk() 
 
main.geometry("500x500") 
main.title("My Chat Bot") 
def ask_from_bot(): 
    query=textF.get() 
    answer_from_bot=bot.get_response(query) 
    msgs.insert(END,"you: "+query) 
    msgs.insert(END,"bot: "+str(answer_from_bot)) 
    speak(answer_from_bot) 
    textF.delete(0,END) 
frame=Frame(main) 
sc=Scrollbar(frame) 
msgs=Listbox(frame,width=80,height=20,yscrollcommand=sc.set) 
sc.pack(side=RIGHT,fill=Y) 
msgs.pack(side=LEFT,fill=BOTH,pady=10) 
frame.pack() 
textF=Entry(main,font=("Verdana",15)) 
textF.pack(fill=X,pady=10) 
btn=Button(main,text="Ask from bot",font=("Verdana",20),command=ask_from_bot) 
btn.pack() 
def enter_function(event): 
    btn.invoke() 
main.bind('<Return>',enter_function) 
 
main.mainloop() 
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    