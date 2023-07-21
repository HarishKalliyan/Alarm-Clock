from threading import Thread
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime
from pygame import mixer 
from time import sleep

#Design
back= '#1f8384'
cl='#59ebcb'
df='#ff74d9'


window=Tk()
window.title("Alarm Clock")
window.geometry('380x180')
window.configure(bg=cl)


top=Frame(window,width=400,height=5,bg='#34495e')
top.grid(row=0,column=0)

bd=Frame(window,width=400,height=200,bg='#F6F3E4')
bd.grid(row=1,column=0)

#Import Icon and Labels

img=Image.open('clock.png')
img.resize((1000,1000))
img=ImageTk.PhotoImage(img)

app=Label(bd,height=200,width=150,image=img,bg='#CFE5FD')
app.place(x=1,y=0)

ala=Label(bd,text="Alarm",width=14,font=('Ivy 20 bold'),bg='#F6F3E4',fg='#F16F6E')
ala.place(x=155,y=10)


hr=Label(bd,text="Hour",height=2,font=('Ivy 15 bold'),bg='#F6F3E4',fg='#F16F6E')
hr.place(x=155,y=40)
hrc=Combobox(bd,width=2,font=('arial 15'))
hrc.place(x=160,y=98)
hrc['values']=('00','01','02','03','04','05','06','07','08','09','10','11','12')
hrc.current(0)


min=Label(bd,text="Min",height=2,font=('Ivy 15 bold'),bg='#F6F3E4',fg='#F16F6E')
min.place(x=210,y=40)
minc=Combobox(bd,width=2,font=('arial 15'))
minc.place(x=210,y=98)
minc['values']=('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
minc.current(0)



sec=Label(bd,text="Sec",height=2,font=('Ivy 15 bold'),bg='#F6F3E4',fg='#F16F6E')
sec.place(x=265,y=40)
secc=Combobox(bd,width=2,font=('arial 15'))
secc.place(x=265,y=98)
secc['values']=('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
secc.current(0)

pd=Label(bd,text="Period",height=2,font=('Ivy 15 bold'),bg='#F6F3E4',fg='#F16F6E')
pd.place(x=310,y=40)
pdc=Combobox(bd,width=3,font=('arial 15'))
pdc.place(x=320,y=98)
pdc['values']=('AM','PM')
pdc.current(0)


#Code part
def active():
    l=Thread(target=alarm)
    l.start()

def deactive():
    print("---------------------Alarm Stopped---------------")
    mixer.music.stop()

selected=IntVar()
rad1=Radiobutton(bd,font=('arial 10 bold'),value=1,text="Activate",bg='#F6F3E4',command=active,variable=selected)
rad1.place(x=175,y=140)


def music():
    mixer.music.load('Alarm.mp3')
    mixer.music.play()
    selected.set(0)

    rad2=Radiobutton(bd,font=('arial 10 bold'),value=2,text="Deactivate",bg='#F6F3E4',command=deactive,variable=selected)
    rad2.place(x=250,y=140)


def alarm():
    while True:
        control=selected.get()
        ahr=hrc.get()
        amin=minc.get()
        asec=secc.get()
        aper=str(pdc.get()).upper()


        now=datetime.now()

        hour=now.strftime("%I")
        mint=now.strftime("%M")
        seo=now.strftime("%S")
        period=now.strftime("%p")


        if control==1:
            if ahr==hour:
                if aper==period:
                    if amin==mint:
                        if asec==seo:
                            print("----------------Wake up--------------")
                            music()
        sleep(1)

mixer.init()

window.mainloop()