from tkinter import *

class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        if self["state"] == "normal":
            self['background'] = self['highlightcolor']

    def on_leave(self, e):
        if self["state"] == "normal":
            self['background'] = self.defaultBackground

def game(x):
    c = 0
    global c2
    d = True
    global end
    end = True
    global Hid
    global wor
    global enable
    while (c<len(Hid)):
        if word[c] == x:
            Hid = Hid[:c] + x + Hid[c+1:]
            d = False
        if Hid[c]=='_':
            end = False
        c+=1
    wor['text']=Hid
    
    if d:
        c2+=1
        match c2:
            case 1:    
                mhead = man.create_oval(ws*0.255,hs*0.2,ws*0.295,hs*0.28,fill="burlywood3",outline="gray", width=2)
            case 2:    
                mbody = man.create_line(ws*0.275,hs*0.28,ws*0.275,hs*0.475,fill="gray", width=2)
            case 3:    
                mhand1 = man.create_line(ws*0.275,hs*0.32,ws*0.24,hs*0.395,fill="gray", width=2)
            case 4:    
                mhand2 = man.create_line(ws*0.275,hs*0.32,ws*0.31,hs*0.395,fill="gray", width=2)
            case 5:    
                mleg1 = man.create_line(ws*0.275,hs*0.475,ws*0.24,hs*0.55,fill="gray", width=2)
            case 6:    
                mleg2 = man.create_line(ws*0.275,hs*0.475,ws*0.31,hs*0.55,fill="gray", width=2)
            case 7:    
                mtext1 = man.create_text(ws*0.267,hs*0.227,fill="gray",text="x",font=("Arial", int(hs*0.025), "bold"))
                mtext2 = man.create_text(ws*0.283,hs*0.227,fill="gray",text="x",font=("Arial", int(hs*0.025), "bold"))
                wor['text']='You Lost!!'
                enable = False
    man.grid(row=1, column=0, columnspan=6, rowspan=9)
    if end:
        wor['text']='You Win!!'
        enable = False

enable = True
root = Tk()
root.configure(bg="white")
root.title("Hangman by Arth")

ws = int(root.winfo_screenwidth()*0.88)
hs = int(ws/2)
x = int((root.winfo_screenwidth() - ws)/2) 
y = int((root.winfo_screenheight() - hs)/2) - int((root.winfo_screenheight() - hs)/10)
root.geometry('%dx%d+%d+%d' % (ws, hs, x, y))

root2 = Toplevel(root)
root2.configure(bg='white')
root2.title("Word")
root2.transient(root)
root2.grab_set()
ws2 = int(ws * 0.7)
hs2 = int(hs/5)
x2 = int((root2.winfo_screenwidth() - ws2)/2) 
y2 = int((root2.winfo_screenheight() - hs2)/2) - int((root2.winfo_screenheight() - hs2)/10)
root2.geometry('%dx%d+%d+%d' % (ws2, hs2, x2, y2))

word = ''
def submit():
    global word 
    word = word_var.get().upper()
    global Hid
    global wor
    for a in word:
        if a==' ':
            Hid+=' '
        elif a.isalpha():
            Hid+='_'
        else:
            Hid = "Only alphabets"
            break
    wor = Label(root, text=Hid, bg="white", font=("Baskerville old face", int(hs*0.075)), wraplength=lf.winfo_width()-5)
    wor.place(in_=lf, anchor=CENTER,relx=0.5,rely=0.5)
    root2.destroy()
word_var = StringVar()
l1 = Label(root2, bg="white", text="Word for hangman: ")
l1.grid(row=1,column=0,padx=(5,0))
entr = Entry(root2, textvariable=word_var, bg="white")
entr.grid(row=1,column=1,columnspan=3, sticky='nsew',padx=(0,5))
subm = Button(root2, text= "Play!", command = submit)
subm.grid(row=2,column=2,pady=(3,0))
root2.columnconfigure(1, weight=1)
root2.columnconfigure(2, weight=1)
root2.columnconfigure(3, weight=1)
root2.rowconfigure(0, weight=1)
root2.rowconfigure(3, weight=1)
root2.resizable(True,False)
def disable_event():
   pass
root2.protocol("WM_DELETE_WINDOW", disable_event)


tif = Frame(width=ws, height=int(hs*0.1), bg="white", borderwidth=0, highlightthickness=0)
tif.grid(row=0, column=0, columnspan=15)
lf = Frame(width=int(ws*0.6), height=int(hs*0.4), bg="white", borderwidth=0, highlightthickness=0)
lf.grid(row=1, column=6, columnspan=9, rowspan=4)

hang = Label(root, bg= "WHITE", text="HANGMAN", font=("Chiller", int(hs*0.075), "bold"), padx=0, pady=0)
hang.place(in_=tif, relx=0.5, rely=0.5, anchor=CENTER)

man = Canvas(root, width=int(ws*0.4), height=int(hs*0.9), bg = "white", borderwidth=0, highlightthickness=0)
base = man.create_line(ws*0.05,hs*0.7,ws*0.15,hs*0.7,fill="black", width=4)
post1 = man.create_line(ws*0.1,hs*0.7,ws*0.1,hs*0.1,fill="black", width=4)
post2 = man.create_line(ws*0.1,hs*0.1,ws*0.275,hs*0.1,fill="black", width=4)
post3 = man.create_line(ws*0.1,hs*0.16,ws*0.13,hs*0.1,fill="black", width=2)
rope = man.create_line(ws*0.275,hs*0.1,ws*0.275,hs*0.2,fill="black", width=4)
man.grid(row=1, column=0, columnspan=6, rowspan=9)

Hid = ''
c2 = 0

b={}
i = 'A'
count = 0
while (i<='Z'):
    def which_button(x = i):
        if enable:
            b[x]["state"]="disabled"
            b[x]['background']='sea green'
            b[x]['disabledforeground']='LightSteelBlue3'
            game(x)
    b[i] = HoverButton(root, text=i, font=("Baskerville old face", int(hs*0.025), 'bold'), command=which_button, bg='dodger blue', activebackground='cyan', highlightcolor='turquoise')
    b[i].grid(row=6+int(count/9), column=6+(count%9),sticky="nsew",padx=hs*0.01,pady=hs*0.01)
    i= chr(ord(i)+1)
    count+=1

root.resizable(False,False)
root.mainloop()