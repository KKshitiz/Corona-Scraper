from tkinter import LEFT,RIGHT,PhotoImage,Tk
from tkinter.ttk import Label,Frame,Button,Treeview,Scrollbar
import tkinter.font as tkFont
from scraper import *

#sets the initial mode of app
mode="app"
#sets initial theme of app
theme="light"

#put the path of the directory where the data file will be stored
path="C:\\Users\\skili\\Documents\\GitHub\\Corona-Scraper\\"


#exits the app gui
def exitAppGui():
    root_app.destroy()



#exits the widget gui
def exitWidgetGui():
    root_widget.destroy()



#set the mode to application mode
def appMode():
    #if widget is displayed destroy it
    if 'root_widget' in globals():
        exitWidgetGui()
    global root_app
    root_app=Tk()
    root_app.title('  Corona-Scraper')
    root_app.iconphoto(True,PhotoImage(file=path+"icon.png"))
    root_app.tk.call('tk','scaling',1.3)
    root_app.attributes('-topmost',0)
    root_app.overrideredirect(0)
    root_app.geometry("{0}x{1}+0+0".format(root_app.winfo_screenwidth(), root_app.winfo_screenheight()))
    listbox=MultiColumnListboxApp()
    root_app.mainloop()



#set the mode to widget mode
def widgetMode():
    if 'root_app' in globals():
        exitAppGui()
    global root_widget
    root_widget=Tk()
    # root_widget.geometry("300x250")
    root_widget.attributes('-topmost',1)
    root_widget.overrideredirect(1)
    root_widget.geometry("300x250+{0}+{1}".format(root_widget.winfo_screenwidth()-300-30, 0+30))
    root_widget.tk.call('tk','scaling',1.3)
    listbox2=MultiColumnListboxWidget()
    root_widget.mainloop()



#function to load data in the starting
def loadData():
    global country_header,country_list
    try:
        rows=readFromCsv(path)
        country_header = rows[0]
        country_list = rows[1:]
    except:
        rows=[["NA"]*6]
        country_header = rows[0]
        country_list = rows[1:]



#function to refresh the data
def refreshData():
    try:
        connect()
        rows=scrape()
        writeToCsv(rows,path)
        loadData()
        print("successfully updated")
    except:
        pass



#function to change application modes
def changeMode():

    global mode
    if mode=="app":
        mode="widget"
        modeb.configure(text="App Mode")
        widgetMode()
        refreshData()
    else:
        mode="app"
        modeb.configure(text="Widget Mode")
        appMode()
        refreshData()



#function to change to dark mode
def darkThemeApp():
    root_app.configure(bg="black")



#function to change to light theme
def lightThemeApp():
    root_app.configure(bg="white")



#function to change to dark mode
def darkThemeWidget():
    root_widget.configure(bg="black")



#function to change to light theme
def lightThemeWidget():
    root_widget.configure(bg="white")




#function to toggle themes
def changeTheme():
    global theme
    if theme=="light":
        theme="dark"
        themeb.configure(text="Light Theme")
        if mode=="app":
            darkThemeApp()
        else:
            darkThemeWidget()

    else:
        theme="light"
        themeb.configure(text="Dark Theme")
        if mode=="app":
            lightThemeApp()
        else:
            lightThemeWidget()



#class to make listbox for appmode
class MultiColumnListboxApp(object):
    """use a ttk.TreeView as a multicolumn ListBox"""

    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        s = "Corona-Scraper"
        msg = Label(wraplength="4i", justify="left", anchor="n",
            padding=(10, 2, 10, 6), text=s)
        msg.pack(fill='x')
        topf=Frame()
        topf.pack(pady=10)
        refreshb=Button(topf,text="Refresh",command=refreshData)
        refreshb.pack(side=LEFT,padx=10)
        global modeb,themeb
        modeb=Button(topf,text="Widget Mode",command=changeMode)
        modeb.pack(side=LEFT,padx=10)
        themeb=Button(topf,text="Dark Mode",command=changeTheme)
        themeb.pack(side=LEFT,padx=10)
        exitb=Button(topf,text="Exit",command=exitAppGui)
        exitb.pack(side=RIGHT,padx=10)

        container = Frame()
        container.pack(fill='both', expand=True)
        # create a treeview with dual scrollbars
        self.tree = Treeview(columns=country_header, show="headings")
        vsb = Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in country_header:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))

        for item in country_list:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(country_header[ix],width=None)<col_w:
                    self.tree.column(country_header[ix], width=col_w)



#inherits app multicolumn list box
class MultiColumnListboxWidget(MultiColumnListboxApp):
    """use a ttk.TreeView as a multicolumn ListBox"""

    def _setup_widgets(self):
        topf=Frame()
        topf.pack()
        refreshb=Button(topf,text="Refresh",command=refreshData)
        refreshb.pack(side=LEFT)
        global modeb,themeb
        modeb=Button(topf,text="App Mode",command=changeMode)
        modeb.pack(side=LEFT)
        themeb=Button(topf,text="Dark Mode",command=changeTheme)
        themeb.pack(side=LEFT)
        exitb=Button(topf,text="Exit",command=exitWidgetGui)
        exitb.pack(side=RIGHT)

        container = Frame()
        container.pack(fill='both', expand=True)
        # create a treeview with dual scrollbars
        self.tree = Treeview(columns=country_header, show="headings")
        vsb = Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)


#sorts the countries based on the header clicked
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



if __name__ == "__main__":
    loadData()
    appMode()