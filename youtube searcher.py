import TERMINALFUNC as tf
import FUNC as f
import webbrowser
import urllib.request
import re

class YtVideo:
	def __init__(self,linkOrId):
		if linkOrId.startswith("http"):
			self.id=getVideoIds(linkOrId)[0]
		else:
			self.id=linkOrId
		self.link="https://www.youtube.com/watch?v="+self.id
		self.page=f.callWeb(self.link)
		self.title=self.page\
					  .replace("<title>","ǉ")\
					  .replace("</title>","ǉ")\
					  .split("ǉ")[1]\
					  .strip(" - YouTube")
	def open(self):
		webbrowser.open(self.link)

def getVideoIds(text):
	return re.findall(r"watch\?v=(\S{11})",text)

def search(query):
	searchLink = "https://www.youtube.com/results?search_query="+query.replace(" ","+")
	results=[]
	for result in getVideoIds(f.callWeb(searchLink)):
		results+=[YtVideo(result)]
	return results

def initScreen():
	tf.raw(enable=True)
	tf.moveCursor(home=True)
	tf.fillWithSpaces(saveCursor=False)
	tf.changeStyle(reset=True)

def unInitScreen():
	tf.raw(disable=True)
	tf.moveCursor(home=True)
	tf.clear(screen=True)
	tf.changeStyle(reset=True)

def halt():
	global keyHandler
	global halting
	halting=True
	keyHandler.halt()
	unInitScreen()

def startKeyHandler():
	global keyHandler
	keyHandler=tf.KeyHandler(
		{
			"q":[halt,()]
		}
	)
	keyHandler.start()

def getTerminalSize():
	global terminalSize
	terminalSize=tf.getTerminalSize()

	global centreOfTerminal
	centreOfTerminal={"row":terminalSize["rows"]//2,"column":terminalSize["columns"]//2}

def getSearch():
	global terminalSize
	global centreOfTerminal
	global results
	global keyHandler
	tf.moveCursor(to={"column":terminalSize["columns"]//5,"row":centreOfTerminal["row"]})
	tf.print(tf.style(color8="cyan",foreground=True)+"What do you want to search for?: "+tf.style(reset=True))
	tf.raw(disable=True)
	keyHandler.halt()
	query=input()
	keyHandler.start()
	tf.raw(enable=True)
	tf.clear(screen=True)
	tf.moveCursor(to={"column":(terminalSize["columns"]//2)-(len("searching.....")//2),"row":centreOfTerminal["row"]})
	tf.print("searching.....")
	results=search(query)

def showResults():
	pass

def main():
	global halting
	halting=False
	getTerminalSize()
	initScreen()
	startKeyHandler()
	while not halting:
		getSearch()
		showResults()

main()
