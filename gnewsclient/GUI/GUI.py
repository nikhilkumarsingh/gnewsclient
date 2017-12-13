from tkinter import *
from gnewsclient import gnewsclient
from gnewsclient import utils
from tkinter import ttk


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



tle_frame=Frame(root)
tle_frame.pack()
edition_label = Label(tle_frame, text="Edition: ").grid(row=1, column=0)
edition_query=StringVar()
edition_dropdown = ttk.Combobox(tle_frame, textvariable=edition_query, values=sorted(list(utils.editionMap))).grid(row=1, column=1)
edition_query.set("Select edition")


topic_label = Label(tle_frame, text="Topic: ").grid(row=2, column=0)
topic_query=StringVar()
topic_dropdown = ttk.Combobox(tle_frame, textvariable=topic_query, values=sorted(list(utils.topicMap))).grid(row=2, column=1)
topic_query.set("Select topic")



language_label = Label(tle_frame, text="Language: ").grid(row=3, column=0)
language_query=StringVar()
language_dropdown = ttk.Combobox(tle_frame, textvariable=language_query, values=sorted(list(utils.langMap))).grid(row=3, column=1)
language_query.set("Select language")




location_label= Label(tle_frame,text="Location: ").grid(row=4,column=0)
location_query = StringVar()
location = Entry(tle_frame, textvariable=location_query).grid(row=4, column=1)


root.mainloop()
