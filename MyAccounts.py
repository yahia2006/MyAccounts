from tkinter import *
from tkinter import messagebox
import json
import webbrowser

from tkinter import filedialog
from PIL import Image,ImageTk




def AddUserAccount():
    with open("data.json",'r') as fr:
        data=json.load(fr)
    data.append({'Gmail':inp1.get(),'Password':inp2.get()})

    if inp1.get()!="" and inp2.get()!="":

        with open("data.json",'w') as fw:
            json.dump(data,fw,indent=4)    
        messagebox.showinfo("info","Done Adding Your Account")
    else:
        messagebox.showerror("Error","Please Fill The Data Entry")


def ReadUserAccounts():
    with open("data.json",'r') as f:
        data_list=json.load(f)
        if data_list.__sizeof__()>20:
            messagebox.showinfo("info","Please Select txt file to show the data!")
            file=open(filedialog.askopenfilename(),'w')
            for i in data_list:
                file.write(f"User Gmail : {i['Gmail']}, User Password : {i['Password']} \n \n")
            messagebox.showinfo("Done",f"Done Saving data in file {file.name}")
        else:
            messagebox.showerror("Error","There is no accounts founded here please add your accounts first !")











app=Tk()
app.title("MyAccounts")

app.geometry("700x500+250+200")


app.config(background='white')

app.resizable(False,False)

app.iconbitmap('imgs\\icon.ico')

pt1=ImageTk.PhotoImage(Image.open('imgs\\applogo2.png'))
lab1=Label(image=pt1,bg='white')
lab1.pack()


lab2=Label(text="Gmail",fg='#111',bg='white',font=(12,12),pady=10)
lab2.pack()

inp1=Entry(width=70,bd=5,justify='center')
inp1.pack()

lab3=Label(text="Password",fg='#111',bg='white',font=(12,12),pady=10)
lab3.pack()

inp2=Entry(width=70,bd=5,justify='center')
inp2.pack()

btn=Button(width=35,text="Save Account",command=AddUserAccount,bd=0,fg='white',bg='green',font=(14,14))
btn.place(x=0,y=465)
btn2=Button(width=35,text="Show Accounts",command=ReadUserAccounts,bd=0,fg='white',bg='blue',font=(14,14))
btn2.place(x=320,y=465)





app.mainloop()







