import tkinter as tk
import random
U=0;li=[];O=0;le=[];max=0;p=0;li2=[];le2=[];lg=[]
#======================================
def salir():
    for x in range(49):
        global max
        if max==10 or max>10:
            li[x-1].configure(state=tk.DISABLED)
            li2[x-1].configure(state=tk.NORMAL)
            btsalir.configure(state=tk.DISABLED)
        else:
            lbl1.configure(text="    FALTAN BARCOS",font=("Arial",14))
def colocar(z):
    global max
    if le[z-1]==0:
        if max<10:
            max=max+1
            le[z-1]=1
            li[z-1].configure(bg="black")
            lbl1.configure(text="Pantalla de barcos: "+str(max)+"/10",font=("Arial",14))
    elif le[z-1]==1:
        max=max-1
        li[z-1].configure(bg="blue")
        lbl1.configure(text="Pantalla de barcos: "+str(max)+"/10",font=("Arial",14))
        le[z-1]=0
def disparar(z):
    if le2[z-1]==0 or le2[z-1]==1:
        if le2[z-1]==0:
            le2[z-1]=3
            li2[z-1].configure(bg="white")
        elif le2[z-1]==1:
            li2[z-1].configure(bg="red")
            le2[z-1]=4
        t=0
        while t!=1:
            t=t+1
            rd=random.randint(0,48)
            if le[rd]==0 or le[rd]==1:
                if le[rd]==1:
                    le[rd]=4
                    li[rd].configure(bg="red")
                elif le[rd]==0:
                    le[rd]=3
                    li[rd].configure(bg="white")
            else:
                t=0
    per=0;gan=0;fi=0
    for x in range(49):
        if le[x]==4:
            per=per+1
        if le2[x]==4:
            gan=gan+1
    if per==10 and gan==10:
        lg.append("EMPATE")
        for x in range(49):
            li2[x].configure(state=tk.DISABLED)
        fi=1
    else:
        if per==10:
            lg.append("PERDISTE")
            for x in range(49):
                li2[x].configure(state=tk.DISABLED)
            fi=1
        elif gan==10:
            lg.append("GANASTE")
            for x in range(49):
                li2[x].configure(state=tk.DISABLED)
            fi=1
    global vf
    if fi==1:
        vf=tk.Tk()
        vf.title("Fin de la partida") 
        vf.geometry("285x220")
        lbl=tk.Label(vf,text=lg[0],font=("Arial",22))
        lbl.place(x=65,y=70)
        Reiniciar=tk.Button(vf,text="Reiniciar",command=partida,font=("Arial",16))
        Reiniciar.place(x=80,y=110)
        vf.mainloop()
def partida():
    global li,le,li2,le2,lg,max,vf
    li=[];le=[];li2=[];le2=[];lg=[];max=0
    for x in range(49):
        le.append(0)
        li.append(eval("bt"+str(x+1)))
        le2.append(0)
        li2.append(eval("bta"+str(x+1)))
        li2[x].configure(bg="blue")
        li[x].configure(bg="blue")
        li2[x].configure(state=tk.DISABLED)
        li[x].configure(state=tk.NORMAL)
        lbl1.configure(text="Pantalla de barcos: "+str(max)+"/10")
    w=0
    while w<10:
        w=w+1
        r=random.randint(0,48)
        if le2[r]==0:
            le2[r]=1
        else:
            w=w-1
    vf.destroy()
    btsalir.configure(state=tk.NORMAL)
v1=tk.Tk()
v1.title("Batalla naval (P1)") 
v1.geometry("550x450")
    #============================"barcos(P1)"===================================================
bt1=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(1),font=("Arial",14))
bt2=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(2),font=("Arial",14))
bt3=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(3),font=("Arial",14))
bt4=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(4),font=("arial",14))
bt5=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(5),font=("Arial",14))
bt6=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(6),font=("Arial",14))
bt7=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(7),font=("Arial",14))
bt8=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(8),font=("Arial",14))
bt9=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(9),font=("Arial",14))
bt10=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(10),font=("Arial",14))
bt11=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(11),font=("Arial",14))
bt12=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(12),font=("Arial",14))
bt13=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(13),font=("Arial",14))
bt14=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(14),font=("Arial",14))
bt15=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(15),font=("Arial",14))
bt16=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(16),font=("Arial",14))
bt17=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(17),font=("Arial",14))
bt18=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(18),font=("Arial",14))
bt19=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(19),font=("Arial",14))
bt20=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(20),font=("Arial",14))
bt21=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(21),font=("Arial",14))
bt22=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(22),font=("Arial",14))
bt23=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(23),font=("Arial",14))
bt24=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(24),font=("Arial",14))
bt25=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(25),font=("Arial",14))
bt26=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(26),font=("Arial",14))
bt27=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(27),font=("Arial",14))
bt28=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(28),font=("Arial",14))
bt29=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(29),font=("Arial",14))
bt30=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(30),font=("Arial",14))
bt31=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(31),font=("Arial",14))
bt32=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(32),font=("Arial",14))
bt33=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(33),font=("Arial",14))
bt34=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(34),font=("Arial",14))
bt35=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(35),font=("Arial",14))
bt36=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(36),font=("Arial",14))
bt37=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(37),font=("Arial",14))
bt38=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(38),font=("Arial",14))
bt39=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(39),font=("Arial",14))
bt40=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(40),font=("Arial",14))
bt41=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(41),font=("Arial",14))
bt42=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(42),font=("Arial",14))
bt43=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(43),font=("Arial",14))
bt44=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(44),font=("Arial",14))
bt45=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(45),font=("Arial",14))
bt46=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(46),font=("Arial",14))
bt47=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(47),font=("Arial",14))
bt48=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(48),font=("Arial",14))
bt49=tk.Button(v1,text="   ",bg="blue",command=lambda:colocar(49),font=("Arial",14))
#============================"barcos(P2)"=======================================================
lbl=tk.Label(v1,text="Pantalla de ataque",font=("Arial",22))
bta1=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(1),font=("Arial",16))
bta2=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(2),font=("Arial",16))
bta3=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(3),font=("Arial",16))
bta4=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(4),font=("arial",16))
bta5=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(5),font=("Arial",16))
bta6=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(6),font=("Arial",16))
bta7=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(7),font=("Arial",16))
bta8=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(8),font=("Arial",16))
bta9=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(9),font=("Arial",16))
bta10=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(10),font=("Arial",16))
bta11=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(11),font=("Arial",16))
bta12=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(12),font=("Arial",16))
bta13=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(13),font=("Arial",16))
bta14=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(14),font=("Arial",16))
bta15=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(15),font=("Arial",16))
bta16=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(16),font=("Arial",16))
bta17=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(17),font=("Arial",16))
bta18=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(18),font=("Arial",16))
bta19=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(19),font=("Arial",16))
bta20=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(20),font=("Arial",16))
bta21=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(21),font=("Arial",16))
bta22=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(22),font=("Arial",16))
bta23=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(23),font=("Arial",16))
bta24=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(24),font=("Arial",16))
bta25=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(25),font=("Arial",16))
bta26=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(26),font=("Arial",16))
bta27=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(27),font=("Arial",16))
bta28=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(28),font=("Arial",16))
bta29=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(29),font=("Arial",16))
bta30=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(30),font=("Arial",16))
bta31=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(31),font=("Arial",16))
bta32=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(32),font=("Arial",16))
bta33=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(33),font=("Arial",16))
bta34=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(34),font=("Arial",16))
bta35=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(35),font=("Arial",16))
bta36=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(36),font=("Arial",16))
bta37=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(37),font=("Arial",16))
bta38=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(38),font=("Arial",16))
bta39=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(39),font=("Arial",16))
bta40=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(40),font=("Arial",16))
bta41=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(41),font=("Arial",16))
bta42=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(42),font=("Arial",16))
bta43=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(43),font=("Arial",16))
bta44=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(44),font=("Arial",16))
bta45=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(45),font=("Arial",16))
bta46=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(46),font=("Arial",16))
bta47=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(47),font=("Arial",16))
bta48=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(48),font=("Arial",16))
bta49=tk.Button(v1,text="    ",bg="blue",command=lambda:disparar(49),font=("Arial",16))
#===================================================================================
btsalir=tk.Button(v1,text="Confirmar",command=salir,font=("Arial",14))
lbl1=tk.Label(v1,text="Pantalla de barcos: 0/10",font=("Arial",14))
lbl1.place(x=300,y=25)
for x in range(49):
    le.append(0)
    li.append(eval("bt"+str(x+1)))
for y in range(50,260,30):
    for x in range(300,496,28):
        eval("bt"+str(p+1)).place(x=x,y=y)
        p=p+1
lbl.grid(column=0,row=0,columnspan=7)
btsalir.place(x=350,y=270)
p=0
for y in range(50,320,40):
    for x in range(10,290,40):
        eval("bta"+str(p+1)).place(x=x,y=y)
        p=p+1
for x in range(49):
    le2.append(0)
    li2.append(eval("bta"+str(x+1)))
    li2[x].configure(state=tk.DISABLED)
w=0
while w<10:
    w=w+1
    r=random.randint(0,48)
    if le2[r]==0:
        le2[r]=1
    else:
        w=w-1
v1.mainloop()