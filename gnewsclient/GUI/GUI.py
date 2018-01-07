from tkinter import *
from gnewsclient import gnewsclient
from gnewsclient import utils
from tkinter import ttk
from PIL import Image
import urllib.request
import webbrowser

def gotolink(event, x):
    webbrowser.open_new(x)


class resizingCanvas(Canvas):
    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)
        self.configure(scrollregion=self.bbox('all'))

    # def canvas_configure(self, event):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()



# function to load news in the east frame(level 1)
# see line numbers 189-234 for detailed explanation
def show_news():
    global east_frame, myscrollbar, frame,canvas, photo
    east_frame.destroy() # destroy old news' frame
    east_frame = Frame(root, relief=GROOVE, bd=1) # new frame for fresh news
    east_frame.pack(side=RIGHT)

    canvas = resizingCanvas(east_frame)

    frame = Frame(canvas)
    myscrollbar = Scrollbar(east_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)
    myscrollbar.pack(side="right", fill="y")

    canvas.pack(side="left", padx=30, pady=30)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    nws = client.get_news()

    l = len(nws)
    photo = {}
    for i in range(l):
        try:
            imzlnk = nws[i]['img']
            imz = Image.open(urllib.request.urlopen(imzlnk))
            imz.save('file' + str(i) + '.gif')
            f = Frame(frame)
            lnk = nws[i]['link']
            ttle = nws[i]['title']
            photo[i] = PhotoImage(file='file' + str(i) + '.gif')
            photolabel = Label(f, image=photo[i]).grid(row=0, column=0, rowspan=3, sticky=W, pady=10)
            ttlelabel = Label(f, text=str(ttle), font=("Helvetica", 12)).grid(row=0, column=1, sticky=W, pady=10)
            read_more = Label(f, text="Read more about this", fg="blue", cursor="hand2")
            read_more.grid(row=1, column=1, sticky=W)
            read_more.bind("<Button-1>", lambda event, link=str(lnk): gotolink(event, link))
            f.grid(column=1, row=i, sticky=W)
        except AttributeError:
            imzlnk = nws[i]['img']
            f = Frame(frame)
            lnk = nws[i]['link']
            ttle = nws[i]['title']
            ttlelabel = Label(f, text=str(ttle), font=("Helvetica", 12)).grid(row=0, column=1, sticky=W)
            read_more = Label(f, text="Read more about this", fg="blue", cursor="hand2")
            read_more.grid(row=1, column=1, sticky=W)
            read_more.bind("<Button-1>", lambda event, link=str(lnk): gotolink(event, link))
            f.pack()
    return





# function to set attributes(language, location, topic), and then fetch news accordingly
# we have variables topic_query, language_query, location_query for storing attributes
def news():
    global location_query, language_query,topic_query,edition_query,client,status
    client.query=None # because search query overrides all other parameters
    client.topic=topic_query.get()
    if(client.topic=="Select topic"):
        client.topic = "top stories"

    client.language=language_query.get()
    if(client.language=="Select language"):
        client.language="english"
    client.edition=edition_query.get()
    if(client.edition == "Select edition"):
        client.edition = "United States (English)"

    client.location= location_query.get()
    if(client.location==""):
        client.location = None

    update_status(client,status)
    show_news()
    return


# to search news related to a search string
def search():
    global search_query,client,status
    client.query= search_query.get()
    update_status(client,status)
    # print(client.get_news())
    show_news()
    return

# helper function for status bar
def getstatus(clientX):
    x = clientX.get_config()
    y=sorted(x)
    text = ""
    for i in y:
        text += str(i) + ": " + str(x[i]) + "                         "
    return text

# set status bar text
def update_status(client, status):
    status['text']=getstatus(client)
    return



#initializing window
root = Tk()
root.title("GNEWSCLIENT")

#object making and packing
client = gnewsclient()
status = Label(root, text=getstatus(client), bd=1, relief=SUNKEN)
status.pack(side=BOTTOM, fill=X)


# implementing searching news
search_frame=Frame(root)
search_frame.pack()
search_query = StringVar()
query = Entry(search_frame, textvariable=search_query).grid(row=1, column=0)
search_button = Button(search_frame,text= "search", command=search).grid(row=1, column = 1)

west_frame = Frame(root)
west_frame.pack(side=LEFT, padx=10)


# frame for topic, location, and edition filters
tle_frame=Frame(west_frame)
tle_frame.pack()

# implementing edition filter
edition_label = Label(tle_frame, text="Edition: ").grid(row=1, column=0,pady=50,sticky=W)
edition_query=StringVar()
edition_dropdown = ttk.Combobox(tle_frame, textvariable=edition_query, values=sorted(list(utils.editionMap))).grid(row=1, column=1,pady=50)
edition_query.set("Select edition")

# implementing topic filter
topic_label = Label(tle_frame, text="Topic: ").grid(row=2, column=0,pady=50,sticky=W)
topic_query=StringVar()
topic_dropdown = ttk.Combobox(tle_frame, textvariable=topic_query, values=sorted(list(utils.topicMap))).grid(row=2, column=1,pady=50)
topic_query.set("Select topic")


# implementing language filter
language_label = Label(tle_frame, text="Language: ").grid(row=3, column=0,pady=50,sticky=W)
language_query=StringVar()
language_dropdown = ttk.Combobox(tle_frame, textvariable=language_query, values=sorted(list(utils.langMap))).grid(row=3, column=1,pady=50)
language_query.set("Select language")



# implementing location filter
location_label= Label(tle_frame,text="Location: ").grid(row=4,column=0,pady=50,sticky=W)
location_query = StringVar()
location = Entry(tle_frame, textvariable=location_query).grid(row=4, column=1,pady=50)

# frame to enclose all the stuff related to show news(level 1)
east_frame=Frame(root,relief=GROOVE,bd=1)
east_frame.pack(side=RIGHT)

# canvas which keeps the news related stuff(level 2)
canvas = resizingCanvas(east_frame)

# the frame inside canvas which shows news and stuff(level 3)
frame = Frame(canvas)
# scrollbar so that the canvas can be scrolled(level 2)
myscrollbar=Scrollbar(east_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)
myscrollbar.pack(side="right",fill="y")

canvas.pack(side="left", padx=30, pady=30)
canvas.create_window((0,0),window=frame,anchor='nw')

# news list which has dictionaries for different news articles
nws = client.get_news() # has the default filtering parameters
l = len(nws)
photo = {} # dictionary which maps numbers with PhotoImage objects
for i in range(l):
    try:
        imzlnk = nws[i]['img']
        imz = Image.open(urllib.request.urlopen(imzlnk))
        imz.save('file'+str(i)+'.gif')
        f = Frame(frame) # frame to display a news article(one frame per article)(level 4)
        lnk = nws[i]['link']
        ttle = nws[i]['title']
        photo[i] = PhotoImage(file='file'+str(i)+'.gif')
        photolabel = Label(f, image = photo[i]).grid(row=0, column=0, rowspan=3, sticky=W, pady=10)
        ttlelabel = Label(f, text=str(ttle), font=("Helvetica", 12)).grid(row=0, column=1, sticky=W, pady=10, padx=5)
        # ttlelabel.config()
        read_more = Label(f, text="Read more about this", fg="blue", cursor="hand2")
        read_more.grid(row=1, column=1, sticky=W, padx=5)
        read_more.bind("<Button-1>", lambda event, link=str(lnk): gotolink(event, link))
        f.grid(column=1, row=i, sticky=W)
    except AttributeError:# incase there is no photo found, no photo rendering done here
        imzlnk = nws[i]['img']
        f = Frame(frame)
        lnk = nws[i]['link']
        ttle = nws[i]['title']
        ttlelabel = Label(f, text=str(ttle), font=("Helvetica", 12)).grid(row=0, column=1, sticky=W)
        read_more = Label(f, text="Read more about this", fg="blue", cursor="hand2")
        read_more.grid(row=1, column=1, sticky=W)
        read_more.bind("<Button-1>", lambda event, link=str(lnk): gotolink(event, link))
        f.pack()

# button to fetch news
getnews = Button(tle_frame, command=news,text = "Get News!").grid(row=6,column=0,columnspan=2, pady=25)
img = PhotoImage(file='logo.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.mainloop()
