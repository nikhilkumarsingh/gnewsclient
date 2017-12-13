from tkinter import *
from gnewsclient import gnewsclient
from gnewsclient import utils

def getstatus(clientX):
    x = clientX.get_config()
    y=sorted(x)
    text = ""
    for i in y:
        text += str(i) + ": " + str(x[i]) + "                         "
    return text

def update_status(client, status):
    status['text']=getstatus(client)
    return


root = Tk()
root.title("GNEWSCLIENT")

client = gnewsclient()
status = Label(root, text=getstatus(client), bd=1, relief=SUNKEN)
status.pack(side=BOTTOM, fill=X)


root.mainloop()
