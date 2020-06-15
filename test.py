import tkinter
from tkinter import*

m=tkinter.Tk()
m.title('course registration')



x=Label(m,text='NAME').grid(row=2,column=0)
w1=Entry(m, text='Name').grid(row=2,column=1)
Y=Label(m,text='USN').grid(row=3,column=0)
w2=Entry(m, text='USN').grid(row=3,column=1)
Z=Label(m,text='Section').grid(row=4,column=0)
w3=Entry(m, text='Section').grid(row=4,column=1)

a=Label(m,text='Subject').grid(row=5,column=0)
b=Label(m,text='REG type').grid(row=5,column=1)
c=Label(m,text='Attempts').grid(row=5,column=2)
d=Label(m,text='Credits').grid(row=5,column=3)

def rowss():
    w=int(input("enter number of year"))
    row=17
    for i in range (1,w):
        ai=Entry(m, text='year i').grid(row=row+1,column=0)
rowss()

a1=Entry(m, text='Subject1').grid(row=6,column=0)
a2=Entry(m, text='Subject2').grid(row=7,column=0)
a3=Entry(m, text='Subject3').grid(row=8,column=0)
a4=Entry(m, text='Subject4').grid(row=9,column=0)
a5=Entry(m, text='Subject5').grid(row=10,column=0)
a6=Entry(m, text='Subject6').grid(row=11,column=0)
a7=Entry(m, text='Subject7').grid(row=12,column=0)
a8=Entry(m, text='Subject8').grid(row=13,column=0)
a9=Entry(m, text='Subject9').grid(row=14,column=0)
a10=Entry(m, text='Subject10').grid(row=15,column=0)

b1=Entry(m, text='regtype1').grid(row=6,column=1)
b2=Entry(m, text='regtype2').grid(row=7,column=1)
b3=Entry(m, text='regtype3').grid(row=8,column=1)
b4=Entry(m, text='regtype4').grid(row=9,column=1)
b5=Entry(m, text='regtype5').grid(row=10,column=1)
b6=Entry(m, text='regtype6').grid(row=11,column=1)
b7=Entry(m, text='regtype7').grid(row=12,column=1)
b8=Entry(m, text='regtype8').grid(row=13,column=1)
b9=Entry(m, text='regtype9').grid(row=14,column=1)
b10=Entry(m, text='regtype10').grid(row=15,column=1)

c1=Entry(m, text='attempts1').grid(row=6,column=2)
c2=Entry(m, text='attempts2').grid(row=7,column=2)
c3=Entry(m, text='attempts3').grid(row=8,column=2)
c4=Entry(m, text='attempts4').grid(row=9,column=2)
c5=Entry(m, text='attempts5').grid(row=10,column=2)
c6=Entry(m, text='attempts6').grid(row=11,column=2)
c7=Entry(m, text='attempts7').grid(row=12,column=2)
c8=Entry(m, text='attempts8').grid(row=13,column=2)
c9=Entry(m, text='attempts9').grid(row=14,column=2)
c10=Entry(m, text='attempts10').grid(row=15,column=2)

d1=Entry(m, text='credits1').grid(row=6,column=3)
d2=Entry(m, text='credits2').grid(row=7,column=3)
d3=Entry(m, text='credits3').grid(row=8,column=3)
d4=Entry(m, text='credits4').grid(row=9,column=3)
d5=Entry(m, text='credits5').grid(row=10,column=3)
d6=Entry(m, text='credits6').grid(row=11,column=3)
d7=Entry(m, text='credits7').grid(row=12,column=3)
d8=Entry(m, text='credits8').grid(row=13,column=3)
d9=Entry(m, text='credits9').grid(row=14,column=3)
d10=Entry(m, text='credits10').grid(row=15,column=3)


m.mainloop()
