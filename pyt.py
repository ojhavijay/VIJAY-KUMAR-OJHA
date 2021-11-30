from tkinter import*
from tkinter import ttk


class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("UniBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=5,bg='orange',width=615)
        main_frame.pack()

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,text='UNIBOT',font=('arial',30,'bold'),fg='green',bg='white')
        Title_label.pack()

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=5,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=5,bg='white',width=730)
        btn_frame.pack()

        label_1=Label(btn_frame,text="type something",font=('arial',14,'bold'),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('arial',15,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send",font=('arial',15,'bold'),width=8,bg='blue',command=self.send)
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear",command=self.clear,font=('arial',15,'bold'),width=8,bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='green',bg='white')
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)
   #===================FUNCTION DECLARATION==============================================================================


        
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')


    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')


        
    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)

        if (self.entry.get()==''):
            self.msg='Please enter something'
            self.label_11.config(text=self.msg,fg='red')
            

        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red')

        if(self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi, i am UniBot.')


        
        elif (self.entry.get()=="hi"):
            self.text.insert(END,'\n\n'+'Bot: Hi')


        elif (self.entry.get()=="where is LPU?"):
            self.text.insert(END,'\n\n'+'Bot: Phagwara.')

        elif (self.entry.get()=="how is lpu?"):
            self.text.insert(END,'\n\n'+'Bot: Good.')
            

        elif (self.entry.get()=="how many student in cse?"):
            self.text.insert(END,'\n\n'+'Bot: near about 1000.')
        
        elif (self.entry.get()=="who created you?"):
            self.text.insert(END,'\n\n'+'Bot:Vijay and Akshay.')

            
            
        elif (self.entry.get()=="what you do?"):
            self.text.insert(END,'\n\n'+'Bot:I am Unibot, i am here to give you information realted the University.')


        elif (self.entry.get()=="tell me about LPU."):
            self.text.insert(END,'\n\n'+'Bot: LPU ranks among Top 100 Institutions in India: Govt. of India NIRF Ranking 2020 offering diploma, undergraduate, postgraduate and doctorate (Ph.D) courses in Management (BBA/MBA), Engineering (B.Tech/M.Tech), Pharma, Science, Agriculture, Fashion, Law, Journalism, Hotel Management and Computer Application (BCA/MCA)')
        
        
        elif (self.entry.get()=="bye"):
            self.text.insert(END,'\n\n'+'Thank You for chatting!')

        else:
             self.text.insert(END,'\n\n'+'Sorry, try something else')
            
            

        
        


        
        
        

if __name__ == '__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()
    
