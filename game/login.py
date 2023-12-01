from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import Quizzytransition




def main():
	global win
	win=Tk()
	app=Login_Window(win)
	win.mainloop()

class Login_Window:
	def __init__(self,root):
		self.root=root
		self.root.title("Login")
		self.root.geometry("1600x900+0+0")

		# ==========================bg image==========================

		self.bg=ImageTk.PhotoImage(file=r"loginqz.jpeg")
		lbl_bg=Label(self.root,image=self.bg)
		lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


		# ==========================main frame==========================
		
		frame=Frame(self.root,bg="black")
		frame.place(x=530,y=170,width=340,height=450)

		img1=Image.open(r"humanlgn.png")
		img1=img1.resize((100,100),Image.ANTIALIAS)
		self.photoimage1=ImageTk.PhotoImage(img1)
		lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
		lblimg1.place(x=530,y=170,width=340,height=115)

		lgo=Label(frame,text="Let's Go",font=("times new roman",25,"bold"),fg="white",bg="black")
		lgo.place(x=120,y=115)

		# ==========================label and entry==========================

		#----------------row1
		username=lbl=Label(frame,text="Username (Email)",font=("times new roman",20,"bold"),fg="white",bg="black")
		username.place(x=45,y=165)

		self.txtuser=Entry(frame,font=("times new roman", 20, "bold"))
		self.txtuser.place(x=40,y=200,width=270)

		#----------------row2
		password=lbl=Label(frame,text="Password",font=("times new roman",20,"bold"),fg="white",bg="black")
		password.place(x=45,y=245)

		self.txtpass=Entry(frame,font=("times new roman", 20, "bold"),show = '*')
		self.txtpass.place(x=40,y=280,width=270)


		#----------------Log in Button
		loginbtn=Button(command=self.login,text="Log In",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,bg="blue",fg="black",activeforeground="white",activebackground="blue")  
		loginbtn.place(x=635,y=500,width=120, height=35)


		#----------------Sign Up Button
		registerbtn=Button(text="Sign Up",font=("times new roman",12,"bold"),command=self.register_window,borderwidth=0,fg="black",bg="white",activeforeground="white",activebackground="black")  
		registerbtn.place(x=550,y=580,width=120)


		#----------------Forget Password Button
		fgpass=Button(text="Forget Password?",command=self.forgot_password_window,font=("times new roman",12,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="white",activebackground="black")  
		fgpass.place(x=550,y=550,width=120)

	def register_window(self):
		self.new_window=Toplevel(self.root)
		self.app=Register(self.new_window) 




	def login(self):
		if self.txtuser.get()=="" or self.txtpass.get()=="":
			messagebox.showerror("Error","Please fullfill all of the required fields")
		else:
			conn=sqlite3.connect("quizmain.db")
			my_cursor=conn.cursor()
			my_cursor.execute("SELECT * FROM userinfo where email=? and password=?",(
																						self.txtuser.get(),
																						self.txtpass.get()

																				))

			row=my_cursor.fetchone()
			if row==None:
				messagebox.showerror("Error","Incorrect Username or Password")
			else:
				open_main=messagebox.askyesno("YesNo","Do you want to enter a game menu?")
				if open_main>0:
					win.destroy()
					Quizzytransition.gameredirect()
				else:
					if not open_main:
						return
			conn.commit()
			conn.close()



	# ==========================Reset Password==========================
	def reset_password(self):
		if self.combo_security_Q.get()=="Select":
			messagebox.showerror("Error","Select security question",parent=self.root2)
		elif self.txt_security_A.get()=="":
			messagebox.showerror("Error","Please enter the answer",parent=self.root2)
		elif self.txt_newpass.get()=="":
			messagebox.showerror("Error","Please enter the new password",parent=self.root2)
		else:
			conn=sqlite3.connect("quizmain.db")
			my_cursor=conn.cursor()
			qry=("SELECT * FROM userinfo where email=? and securityQ=? and securityA=?")
			inp=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security_A.get(),)
			my_cursor.execute(qry,inp)
			row=my_cursor.fetchone()
			if row==None:
				messagebox.showerror("Error","Answer is incorrect",parent=self.root2)
			else:
				query=("update userinfo set password=? where email=?")
				value=(self.txt_newpass.get(),self.txtuser.get())
				my_cursor.execute(query,value)

				conn.commit()
				conn.close()
				messagebox.showinfo("Info","Your password has been reset successfully",parent=self.root2)
				self.root2.destroy()


	



	# ==========================Forget Password==========================

	def forgot_password_window(self):
		if self.txtuser.get()=="":
			messagebox.showerror("Error","Please enter the Email address to reset password")
		else:
			conn=sqlite3.connect("quizmain.db")
			my_cursor=conn.cursor()
			query=("SELECT * FROM userinfo where email=?")
			value=(self.txtuser.get(),)
			my_cursor.execute(query,value)
			row=my_cursor.fetchone()
			

			if row==None:
				messagebox.showerror("My Error","Please enter the valid Username")
			else:
				conn.close()
				self.root2=Toplevel()
				self.root2.title("Forget Password")
				self.root2.geometry("340x450+610+170")


				l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="black",bg="white")
				l.place(x=0,y=10,relwidth=1)

				security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
				security_Q.place(x=50,y=80)

				self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
				self.combo_security_Q["values"]=("Select", "Your Birth Place", "Your Favorite Color", "Your Pet Name")
				self.combo_security_Q.place(x=50,y=110,width=250)
				self.combo_security_Q.current(0)



				security_A=Label(self.root2,text="Select Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
				security_A.place(x=50,y=150)

				self.txt_security_A=ttk.Entry(self.root2,font=("times new roman",15))
				self.txt_security_A.place(x=50,y=180,width=250)

				new_password=Label(self.root2,text="Type New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
				new_password.place(x=50,y=220)

				self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15),show = '*')
				self.txt_newpass.place(x=50,y=250,width=250)


				btn=Button(self.root2,text="Reset",command=self.reset_password, font=("times new roman",15,"bold"),bg="white",fg="green", )
				btn.place(x=130,y=290)
	






class Register:
	def __init__(self,root):
		self.root=root
		self.root.title("Register")
		self.root.geometry("1600x900+0+0") 

		# ==========================variables==========================
		self.var_fname=StringVar()
		self.var_lname=StringVar()
		self.var_contact=StringVar()
		self.var_email=StringVar()
		self.var_security_Q=StringVar()
		self.var_security_A=StringVar()
		self.var_pass=StringVar()
		self.var_confpass=StringVar()

		# ==========================bg image==========================
		self.bg=ImageTk.PhotoImage(file=r"quizimg1.jpeg")
		bg_lbl=Label(self.root,image=self.bg)
		bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)



		# ==========================main frame==========================
		frame=Frame(self.root,bg="white")
		frame.place(x=320,y=100,width=800,height=550)

		register_lbl=Label(frame,text="SIGN UP",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
		register_lbl.place(x=20,y=20)

		# ==========================label and entry==========================


		#----------------row1
		fname=Label(frame,text="First name",font=("times new roman",15,"bold"),bg="white",fg="black")
		fname.place(x=50,y=100)

		self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
		self.fname_entry.place(x=50,y=130,width=250 )

		l_name=Label(frame,text="Last name",font=("times new roman",15,"bold"),bg="white",fg="black")
		l_name.place(x=370,y=100)

		self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
		self.txt_lname.place(x=370,y=130,width=250)


		#----------------row2
		contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
		contact.place(x=50,y=170)

		self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
		self.txt_contact.place(x=50,y=200,width=250)

		email=Label(frame,text="Email (This also will serve as your Username)",font=("times new roman",15,"bold"),bg="white",fg="black")
		email.place(x=370,y=170)

		self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
		self.txt_email.place(x=370,y=200,width=250)


		#----------------row3
		security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
		security_Q.place(x=50,y=240)

		self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_security_Q,font=("times new roman",15,"bold"),state="readonly")
		self.combo_security_Q["values"]=("Select", "Your Birth Place", "Your Favorite Color", "Your Pet Name")
		self.combo_security_Q.place(x=50,y=270,width=250)
		self.combo_security_Q.current(0)



		security_A=Label(frame,text="Select Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
		security_A.place(x=370,y=240)

		self.txt_security_A=ttk.Entry(frame,textvariable=self.var_security_A,font=("times new roman",15))
		self.txt_security_A.place(x=370,y=270,width=250)


		#----------------row4
		pswrd=Label(frame,text="Set Password",font=("times new roman",15,"bold"),bg="white",fg="black")
		pswrd.place(x=50,y=310)

		self.txt_pswrd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15),show = '*')
		self.txt_pswrd.place(x=50,y=340,width=250)

		pswrd_cnfrm=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
		pswrd_cnfrm.place(x=370,y=310)

		self.txt_pswrd_cnfrm=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15),show = '*')
		self.txt_pswrd_cnfrm.place(x=370,y=340,width=250)



		# ==========================check button==========================
		self.var_check=IntVar()
		checkbut=Checkbutton(frame,variable=self.var_check,text="I Agree To The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1, offvalue=0)
		checkbut.place(x=50,y=380)



		# ==========================buttons==========================
		rgstrbtn=Button(root,text="Sign Up",command=self.register_data,font=("times new roman",15,"bold"),bg="white",fg="black")  
		rgstrbtn.place(x=370,y=530,width=250, height=50)

		loginbtn=Button(root,text="Log In",command=self.login_back,font=("times new roman",15,"bold"),bg="white",fg="black")  
		loginbtn.place(x=690,y=530,width=250, height=50)



	# ==========================Function Declaration==========================
	def register_data(self):
		if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_security_Q.get()=="":
			messagebox.showerror("Error","Please fullfill all of the required fileds")
		elif self.var_pass.get()!=self.var_confpass.get():
			messagebox.showerror("Error","Passwords do not match")
		elif self.var_check.get()==0:
			messagebox.showerror("Error","Please agree to The Terms & Conditions")
		else:
			conn=sqlite3.connect("quizmain.db")
			my_cursor=conn.cursor()
			query=("SELECT * FROM userinfo where email=?")
			value=(self.var_email.get(),)
			my_cursor.execute(query,value)
			row=my_cursor.fetchone()
			if row!=None:
				messagebox.showerror("Error","User already exist, please try to register with another mail address")
			else:
				my_cursor.execute("INSERT INTO userinfo VALUES (?,?,?,?,?,?,?)",(
																						self.var_fname.get(),
																						self.var_lname.get(),
																						self.var_contact.get(),
																						self.var_email.get(),
																						self.var_security_Q.get(),
																						self.var_security_A.get(),
																						self.var_pass.get()

																					))

			conn.commit()
			conn.close()
			messagebox.showinfo("Success","You are successfully signed up!")




	def login_back(self):
		self.root.destroy()









if __name__ == "__main__":
	main()

