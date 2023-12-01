import tkinter
from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox
import time
import multiprocessing




questions=[
	"In which year the Python was first appeared?",
	"Who developed Python Programming Language?",
	"All keywords in Python are in _________",
	"Which of the following is used to define a block of code in Python language?",
	"Which of the following is not a core data type in Python programming?",
	"Which of the following is true for variable names in Python?",
	"Which of the following functions is a built-in function in python?",
	"Which faculty had Ismail Koyuncu graduated from?",
	"What arithmetic operators cannot be used with strings in Python?",
	"The process of pickling in Python includes ____________"
]

answer_choice=[
	["1972","1991","1995","2000"],
	["Brendan Eich","Dennis Ritchie","Linus Torvalds","Guido van Rossum"],
	["Capitalized","lower case","UPPER CASE","None of the mentioned"],
	["Indentation","Key","Brackets","All of the mentioned"],
	["Tuples","Lists","Class","Dictionary"],
	["underscore and ampersand are the only two special characters allowed","unlimited length","all private members must have leading and trailing underscores","none of the mentioned"],
	["factorial()","print()","seed()","sqrt()"],
	["Computeer engineering","Environmental engineering","Civil engineering","Aeronautical engineering"],
	["*","–","+","All of the mentioned"],
	["conversion of a Python object hierarchy into byte stream"," conversion of a datatable into a list","conversion of a byte stream into Python object hierarchy","conversion of a list into a datatable"]
]

asnwers=[1,3,3,1,2,1,1,1,1,0]

player_choice=[]

indexes=[]
start_end_time = []




def countDown():
	start_end_time.append(time.time())
	a=int(time.time())
	while True:
		b = int(time.time())
		c = 100-(b-a)
		timer.configure(text=c)
		root.update()
		time.sleep(0.1)
		if c<=0:
			break	

	calc()

	while calc():
		root.destroy()

	


def generate():
	global indexes
	while(len(indexes)<5):
		x=random.randint(0,9)
		if x in indexes:
			continue
		else:
			indexes.append(x)


def getresult(score):
	global root
	lblquestion.destroy()
	r1.destroy()
	r2.destroy()
	r3.destroy()
	r4.destroy()
	root.destroy()
	start_end_time.append(time.time())
	my_time=start_end_time[1] - start_end_time[0] 



	if score==100:
		messagebox.showinfo("Result","Your score is 100\nYou got A grade\nYour time is: %d" % my_time)
	elif score==80:
		messagebox.showinfo("Result","Your score is 80\nYou got B grade\nYour time is: %d" % my_time)
	elif score==60:
		messagebox.showinfo("Result","Your score is 60\nYou got C grade\nYour time is: %d" % my_time)
	elif score==40:
		messagebox.showinfo("Result","Your score is 40\nYou got D grade\nYour time is: %d" % my_time)
	elif score==20:
		messagebox.showinfo("Result","Your score is 20\nYou got E grade\nYour time is: %d" % my_time)
	else:
		messagebox.showinfo("Result","Your score is 0\nYou got F grade\nYour time is: %d" % my_time)


def calc():
	global indexes,player_choice,asnwers
	x=0
	score=0
	if len(player_choice) == 0:
		getresult(score)
		return 0
	l = len(player_choice)
	for i in range(l, len(indexes)):
		player_choice.append(-1)
	for i in indexes:
		if len(player_choice) < len(indexes):
			break
		if player_choice[x] == asnwers[i]:
			score=score+20

		x+=1
	
	getresult(score)
	return 0



ques=1


def chosen():
	global radiovar,player_choice
	global lblquestion,r1,r2,r3,r4
	global ques
	x=radiovar.get()
	player_choice.append(x)
	radiovar.set(-1)
	if ques < 5:
		lblquestion.config(text=questions[indexes[ques]])
		r1['text']=answer_choice[indexes[ques]][0]
		r2['text']=answer_choice[indexes[ques]][1]
		r3['text']=answer_choice[indexes[ques]][2]
		r4['text']=answer_choice[indexes[ques]][3]
		ques+=1
	else:
		calc()


def startquiz():
	global lblquestion,r1,r2,r3,r4
	lblquestion=Label(root,text=questions[indexes[0]],font=("times new roman", 16, "bold"),background="#888888")
	lblquestion.place(x=550,y=5)


	global radiovar
	radiovar=IntVar()
	radiovar.set(-1)


	r1=Radiobutton(root,command=chosen,text=answer_choice[indexes[0]][0],font=("times new roman", 16, "bold"),value=0,variable=radiovar,background="#888888")
	r1.place(x=550,y=40)

	r2=Radiobutton(root,command=chosen,text=answer_choice[indexes[0]][1],font=("times new roman", 16, "bold"),value=1,variable=radiovar,background="#888888")
	r2.place(x=550,y=70)

	r3=Radiobutton(root,command=chosen,text=answer_choice[indexes[0]][2],font=("times new roman", 16, "bold"),value=2,variable=radiovar,background="#888888")
	r3.place(x=550,y=100)

	r4=Radiobutton(root,command=chosen,text=answer_choice[indexes[0]][3],font=("times new roman", 16, "bold"),value=3,variable=radiovar,background="#888888")
	r4.place(x=550,y=130)


def startbtnprs():
	labelimage.destroy()
	labeltext.destroy()
	btnStart.destroy()
	lblinstructions.destroy()
	lblRules.destroy()
	generate()
	startquiz()
	countDown()
	try:
		root.destroy()
	except:
		time.sleep(0.0001)

	process1 = multiprocessing.Process(target=startgame)
	process2 = multiprocessing.Process(target=countDown)

	process1.start()
	process2.start()




def startgame():
	global root
	global labelimage
	global labeltext
	global lblinstructions
	global btnStart
	global lblRules
	global timer
	root=tkinter.Tk()
	root.title("Quizzy")
	root.geometry("1600x900+0+0")
	root.config(background="#888888")

	img1=ImageTk.PhotoImage(file="quizstart.jpeg")

	labelimage=Label(root,image=img1,background="#888888")
	labelimage.pack(pady=(40,0))

	labeltext=Label(root,text="Quizzy",font=("times new roman",30,"bold"),background="#888888")
	labeltext.pack(pady=(0,50))

	btnStart=Button(root,command=startbtnprs,text="Start",font=("times new roman",16,"bold"),relief=FLAT,border=0)
	btnStart.place(x=660,y=510,width=120, height=35)

	lblinstructions=Label(root,text="Read the rules carefully and\nClick start button once you are ready",background="#888888",foreground="#FACA2F",font=("times new roman",20,"bold"),justify="center")
	lblinstructions.place(x=570,y=600)

	lblRules=Label(root,text="This quiz contains 5 questions\nYou will get total of 100 seconds to solve the question\nOnce you selected radio button that will be a final choice and you will be redirected to the next question\nTherefore think carefully before you make a choice",width=100,font=("times new roman",20,"bold"),background="#888888")
	lblRules.place(x=240,y=678)

	timer = Label(root, background="#888888")
	timer.place(relx=0.8,rely=0.82,anchor=CENTER)

	root.mainloop()