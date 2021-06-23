from tkinter import *
import webbrowser
import urllib.request
import re
app = Tk()
videoIds=""
link=""
searchLen = Label()
def getResults():
    global stringGet
    global text
    global videoIds
    global searchLen
    searchlink = "https://www.youtube.com/results?search_query="
    search=stringGet.get().replace(" ","+")
    searchlink = "https://www.youtube.com/results?search_query="+search
    html = urllib.request.urlopen(searchlink)
    videoIds=re.findall(r"watch\?v=(\S{11})",html.read().decode())
    searchLen.config(text="Results found: "+str(len(videoIds)))
    updateScreen()
def updateScreen():
    global text
    global link
    global videoIds
    global title
    link="https://www.youtube.com/watch?v="+videoIds[pointer]
    page=urllib.request.urlopen(link).read().decode()
    title = page\
        .replace("<title>","ǉ")\
        .replace("</title>","ǉ")\
        .split("ǉ")[1]\
        .strip(" - YouTube")
    text.config(text=str(pointer+1)+"#"+" "+title)
stringGet = Entry(app)
stringGet.pack()
searchButton = Button(app,text="search",command=getResults)
searchButton.pack()
searchLen.pack()
def up():
    global pointer
    if pointer > 0:
        pointer -=1
    updateScreen()
def down():
    global pointer
    if pointer < len(videoIds):
        pointer+=1
    updateScreen()
def openLink():
    webbrowser.open(link)
pointer = 0
title = ""
text=Label()
buttonUp = Button(text="Prev",command=up)
buttonUp.pack()
text.pack()
buttonDown = Button(text="Next",command=down)
buttonDown.pack()
buttonOpen = Button(text="Open",command=openLink)
buttonOpen.pack()
app.mainloop()
