import Tkinter
import tkMessageBox

class Application(Tkinter.Frame):

    def aboutCallBack(self):
        tkMessageBox.showinfo("Just BeWeave", "Alex Lambert - alamb25@uw.edu\nThomas Schmidt - tom5862@uw.edu\nTodd Crane - cranet@uw.edu\nPhansa Chaonpoj -phansac@uw.edu\n")

    def createMenuBar(self):
        self.menuBar = Tkinter.Menu(self)
        self.helpmenu = Tkinter.Menu(self.menuBar, tearoff=0)
        self.helpmenu.add_command(label="About...", command=self.aboutCallBack)
        self.menuBar.add_cascade(label="Help", menu=self.helpmenu)

        root.config(menu=self.menuBar)
    def createWidgets(self):
        self.createMenuBar()
        self.quitButton = Tkinter.Button(self, text="QUIT", fg="red", command=self.quit)
        self.quitButton.pack({"side": "left"})

    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tkinter.Tk()

app = Application(master=root)
app.mainloop()
root.destroy()
