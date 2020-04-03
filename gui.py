from tkinter import *
from tkinter.ttk import *
from scraper import *

#sets the initial mode of app
mode="app"

#put the path of the directory where the data file will be stored
path="C:\\Users\\skili\\Documents\\GitHub\\Corona-Scraper\\"

#exits the corona monitor
def exitGui():
    root.destroy()



#set the mode to application mode
def appMode():
    root.attributes('-topmost',0)
    root.overrideredirect(0)



#set the mode to widget mode
def widgetMode():
    root.attributes('-topmost',1)
    root.overrideredirect(1)



#function to refresh the data
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



def sortby(tree, col, descending):
    #sort tree contents when a column header is clicked on
    # grab values to sort
    data = [(tree.set(child, col), child) \
        for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    #data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, \
        int(not descending)))



#starts the gui
def startGui():
    global root
    root=Tk()
    root.title('  Corona-Scraper')
    root.configure(bg="black")
    root.iconphoto(True,PhotoImage(file=path+"icon.png"))
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