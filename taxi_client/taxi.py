from tkinter import *
from tkinter import messagebox
import os,sys
import requests,random
class Frames(object):


    def exit(self):
        sys.exit()
    
    def journey_started(self):
        messagebox.showinfo("information","Your Journey Has Been Started !") 
   
    def newWindow(self,detail): # new window definition
        newwin = Toplevel(root)
        newwin.title('Dashboard')
        newwin.geometry("500x500") 
        newwin.resizable(0, 0)
        label1 = Label(newwin, text="Welcome to Frame",font="Times")
        label1.pack()
        label5 = Label(newwin, text="Username :- "+detail['name'])
        label5.pack()
        label3 = Label(newwin, text="-------------------------------------------------------------------",font = "Helvetica 16 bold italic")
        label3.pack()
        label4 = Label(newwin,text='Select the Source and Destination')
        label4.pack()
        # display = Label(newwin, text=detail['name'],font='Times')

        sources = ["virar","nalasopara","vasai","palghar"] #etc
        source = StringVar(newwin)
        source.set(sources[0]) # default value
        w = OptionMenu(newwin, source, *sources)
        
        w.pack()

        destinations = ["virar","nalasopara","vasai","palghar"] #etc
        destination = StringVar(newwin)
        destination.set(destinations[0]) # default value
        zz = OptionMenu(newwin, destination, *destinations)
        
        zz.pack()

        lolsource,loldestination = source.get(),destination.get()
        print(lolsource,loldestination)

        button1 = Button(newwin,text="Calculate Fare",command=self.newupdatefare)
        button1.pack()
        # fare = self.fare(selected_source,selected_destination)
        label7 = Label(newwin, text="------------------------------------------------------",font = "Helvetica 16 bold italic").pack()
        
        self.label6 = Label(newwin,text='Your Fare will be :- ',font='Times')
        self.label6.pack()
        label8 = Label(newwin, text="------------------------------------------------------",font = "Helvetica 16 bold italic").pack()
        start_journey_button = Button(newwin, 
                   text="Start Journey",
                   command=self.journey_started
                   )
        start_journey_button.pack()

        exit_button = Button(newwin, 
                   text="Exit",
                   command=self.exit)
        exit_button.pack()


    def newupdatefare(self):
        # return random.randrange(100,200)
        self.label6['text'] = 'Your Fare will be :- Rs.'+str(random.randrange(100,200))



    # DONOT TOUCH
    def login(self,*args,**kwargs):
        resp = requests.get('http://127.0.0.1:8080/matching/scan/',stream=True)
        print(resp.text)
        
        id = ''
        name = ''
        result = resp.text.split(',')
        print('length',len(result[2].split(' ')))
        if result[0] == 'True':
            id = result[1]
            print('id is ',id)
            if(len(result[2].split(' ')) == 1):
                name = result[2][2:len(result[2])-2]
                print('Assigned name ',name)
            else:
                pass
        print("Welcome ",name,"your id is ",id)
        detail = {
            'id' : id,
            'name' : name
        }
        self.newWindow(detail)


    # DONOT TOUCH
    def mainFrame(self,root):
        root.title('FRAME-Taxi Client')
        root.geometry("400x400") 
        root.resizable(0, 0)
        label1 = Label(root, text="FRAME",font = "Helvetica 16 bold italic").pack()
        
        label2 = Label(root, text="Frame Taxi Client",font = "Times").pack()
        label3 = Label(root, text="------------------------------------------------------",font = "Helvetica 16 bold italic").pack()
        # Display image
        label4 = Label(root, text="Scan Your Face to continue",font = "Helvetica 16 bold italic").pack()
        
        button = Button(root, 
                   text="Scan Face",
                   command=self.login)
        button.pack()
        



root = Tk()
app = Frames()
app.mainFrame(root)
root.mainloop()