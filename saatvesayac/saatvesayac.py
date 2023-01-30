from tkinter import *
from time import *
#Saat için bu kütüphaneleri tanımlamak yeterlidir.
import datetime
#Sayaç oluşturabilmek için bu kütüphaneyi de eklememiz gereklidir.


root = Tk()
root.title('KK Saat')

#Saat oluşturmak için gerekli fonksiyon.
def clock():
    text = strftime('%H:%M:%S')
    label.config(text=text)
    label.after(1000,clock)

#Sayaç oluşturmak için gerekli fonksiyon.
def countdown():
   delta = datetime.datetime(2023,1,30,20,49,6) - datetime.datetime.now()
   days = delta.days
   hours , rem = divmod(delta.seconds,3600)
   minutes , seconds = divmod(rem,60)
   text = fillzero(str(hours)) + ":" + fillzero(str(minutes)) + ":" + fillzero(str(seconds))
   label.config(text=text)
   label.after(1000,countdown)

#Sayaçta iki basamaklı sıfırları gelen sayıya göre dolduran fonksiyon.
def fillzero(x):
    return x.zfill(2)

#Oluşturulan saat ve sayaçın stilleri.
label = Label(root,font=("ds-digital",100),background="black",foreground="white")
label.pack(anchor="center")
 

clock()

countdown()


