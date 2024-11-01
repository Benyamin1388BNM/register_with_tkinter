from connect_to_mysql import *
from tkinter import *
from tkinter import messagebox
window=Tk()
window.title('login_member')
window.geometry('600x600')
window.config(bg='pink')
def check_information():
    global entry_register,entry_username,entry_password
    register=entry_register.get()
    username=entry_username.get()
    password=entry_password.get()
    if register=='yes' or register=='Yes':
        try:
            mycursor.execute("SELECT password FROM members WHERE username='"+username+"'")
            List=mycursor.fetchall()
            Tuple=List[0]
            username_password=Tuple[0]
            if password==username_password:
                messagebox.showinfo('welcome','information was True')
                entry_register.delete(0,END)
                entry_username.delete(0,END)
                entry_password.delete(0,END)
            else:
                messagebox.showerror('sorry','password was false')
        except :
            messagebox.showerror('Sorry','information is false')
    elif register=='no' or register=='No':
        if len(username)>2:
            mycursor.execute('SELECT username FROM members')
            usernames_list=mycursor.fetchall()
            for tuple_username in usernames_list:
                if username==tuple_username[0]:
                    messagebox.showerror('sorry','another person used from this username')
                    break
            else:
                if len(password)>6:
                    values=[(username,password)]
                    mycursor.executemany('INSERT INTO members(username,password) VALUES (%s,%s)',values)
                    conn.commit()
                    messagebox.showinfo('welcome','welcome to our family')
                    entry_register.delete(0,END)
                    entry_username.delete(0,END)
                    entry_password.delete(0,END)
                else:
                    messagebox.showerror('password','password is not safe')
        else:
            messagebox.showerror('sorry','username should be greater from 2 letters')
    else:
        messagebox.showerror('Sorry',"I don't underestand your mean! Are you registerid?")
def see():
    global my_button
    global password_button
    global entry_password
    if entry_password.cget('show')=="":
        entry_password.config(show='*')
        password_button.config(text='show password')
    else:
        entry_password.config(show="")
        password_button.config(text='hide password')
text_register=Label(window,bg='green',fg='white',text='Are you register?',font=('arial',16,'bold')).grid(row=1,column=1)
text_username=Label(window,text='username:',font=('arial',16,'bold')).grid(row=2,column=1)
text_password=Label(window,text='password:',font=('arial',16,'bold')).grid(row=3,column=1)
entry_register=Entry(window,font=('arial',16,'bold'))
entry_register.grid(row=1,column=2)
entry_username=Entry(window,font=('arial',16,'bold'))
entry_username.grid(row=2,column=2)
entry_password=Entry(window,show='*',font=('arial',16,'bold'))
entry_password.grid(row=3,column=2)
my_button=Button(window,text='OK',bg='orange',fg='white',font=('arial',16,'bold'),command=check_information)
my_button.grid(row=4,column=3)
password_button=Button(window,text='show paswsword',font=('arial',14,'bold'),command=see)
password_button.grid(row=3,column=3)
exit_button=Button(window,text='EXIT',font=('arial',16,'bold'),bg='red',fg='white',command=lambda :window.destroy())
exit_button.grid(row=1,column=3)
window.mainloop()
