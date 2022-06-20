from tkinter import *
import os.path
from tkinter import scrolledtext

tk = Tk()
path = "C:/Users/user/BusinessTripData.txt"
tk.geometry("1200x600")

mycontainer = Frame(tk)
mycontainer.pack()

top_frame = Frame(mycontainer)
top_frame.pack(fill=BOTH, expand=YES)

left_frame = Frame(top_frame, relief=RIDGE, height=250, width=100)

left_frame.pack(side=LEFT,
                fill=BOTH,
                expand=YES)

right_frame=Frame(top_frame,background="tan",borderwidth=5,relief=RIDGE,width=250)

right_frame.pack(side=RIGHT, fill=BOTH,expand=YES)

scrollbar = Scrollbar(right_frame)
scrollbar.pack(side="right", fill="both")
list = Listbox(right_frame, yscrollcommand=scrollbar.set, width=400, height=1000)
list.pack(side="left", fill="both")
scrollbar.config(command=list.yview)

def fileExists():
    if os.path.isfile(path):
        firstWriteFile()
        print("처음 파일 생성")
    else:
        appendWriteFile()
        print("추가 ")

def readFile():
    f = open(path, 'r')
    tmp = f.readlines()
    list.delete(0, END)
    for item in tmp:
        list.insert(END, item)



def firstWriteFile():
    name = nameEntry.get()
    number = numberEntry.get()
    address = addressEntry.get()
    date = dateEntry.get()
    price = priceEntry.get()
    with open(path, 'w') as f:
        print("fir" + name + number + address + date + price)

        f.write("이름: " + name + "\t" + "  번호: " + number + "\t" + "  주소: " + address + "\t" + "  날짜: " + date + "\t" + "  가격: " + price + "\n")

def appendWriteFile():
    name = nameEntry.get()
    number = numberEntry.get()
    address = addressEntry.get()
    date = dateEntry.get()
    price = priceEntry.get()
    with open(path, 'a') as f:
        print("app"+name + number + address + date + price)
        f.write("이름: "+ name + "\t" +"  번호: "+ number + "\t"+"  주소: "+ address + "\t"+"  날짜: "+ date + "\t"+"  가격: "+ price + "\n")


namelabel = Label(left_frame, text="이름",padx = 50, pady= 10).grid(row=0, column=0)
numberlabel = Label(left_frame, text="번호",padx = 50, pady= 10).grid(row=1, column=0)
addresslabel = Label(left_frame, text="주소",padx = 50, pady= 10).grid(row=2, column=0)
datelabel = Label(left_frame, text="날짜",padx = 50, pady= 10).grid(row=3, column=0)
pricelabel = Label(left_frame, text="가격",padx = 50, pady= 10).grid(row=4, column=0)

nameEntry = Entry(left_frame)
numberEntry = Entry(left_frame)
addressEntry = Entry(left_frame)
dateEntry = Entry(left_frame)
priceEntry = Entry(left_frame)

nameEntry.grid(row=0, column=1)
numberEntry.grid(row=1, column=1)
addressEntry.grid(row=2, column=1)
dateEntry.grid(row=3, column=1)
priceEntry.grid(row=4, column=1)

registerBtn = Button(left_frame, text="등록", bg='green', command=appendWriteFile).grid(row=5, column=0)
readBtn = Button(left_frame, text="파일 읽어오기", bg='red', command=readFile).grid(row=5, column=1)




tk.mainloop()