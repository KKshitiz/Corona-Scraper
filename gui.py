from tkinter import *
from tkinter.ttk import *

mode="app"

def exitGui():
    root.destroy()

def appMode():
    root.attributes('-topmost',0)
    root.overrideredirect(0)

def widgetMode():
    root.attributes('-topmost',1)
    root.overrideredirect(1)

def refreshData():
    return

#function to change application modes
def changeMode():

    global mode
    if mode=="app":
        mode="widget"
        modeb.configure(text="App Mode")
        widgetMode()
    else:
        mode="app"
        modeb.configure(text="Widget Mode")
        appMode()

def startGui():
    global root
    root=Tk()
    root.title('  Corona-Scraper')
    root.configure(bg="black")
    # root.iconphoto(True,PhotoImage(file=""))
    root.tk.call('tk','scaling',1.6)
    root.geometry("400x500")

    topf=Frame(root)
    topf.pack()

    refreshb=Button(topf,text="Refresh",command=refreshData)
    refreshb.pack(side=LEFT)
    global modeb
    modeb=Button(topf,text="Widget Mode",command=changeMode)
    modeb.pack(side=LEFT)
    exitb=Button(topf,text="Exit",command=exitGui)
    exitb.pack(side=RIGHT)


    root.mainloop()

if __name__ == "__main__":
    startGui()