import TERMINALFUNC as tf
import FUNC as f
import webbrowser
import urllib.request
import toascii as ta
import re

class YtVideo:
	def __init__(self,linkOrId):
		if linkOrId.startswith("http"):
			self.id=getVideoIds(linkOrId)[0]
		else:
			self.id=linkOrId
		self.page=f.callWeb("https://www.youtube.com/watch?v="+self.id)
		self.title=self.page\
					  .replace("<title>","ǉ")\
					  .replace("</title>","ǉ")\
					  .split("ǉ")[1]\
					  .strip(" - YouTube")

def getVideoIds(text):
	return re.findall(r"watch\?v=(\S{11})",text)

def search(query):
	searchlink = "https://www.youtube.com/results?search_query="+query.replace(" ","+")
	results=[]
	for result in getVideoIds(f.callWeb(searchLink)):
		results+=YtVideo(result)
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

def playVideo(videoId):
	global terminalSize

	f.downloadWeb("https://www.youtube.com/watch?v="+videoId,"video.mp4")

	frames=ta.VideoConverter(
			"videoplayback.mp4"
			,getScale("videoplayback.mp4"),
			2,
			"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ",
			False
		)\
		.convert().ascii_frames

	f.log("converted")
	tf.moveCursor(home=True)
	tf.fillWithSpaces()
	for frame in frames:
		tf.moveCursor(home=True)
		tf.clear(screen=True)
		tf.print(frame.strip("\n"))
		t.sleep(1/24)

def main():
	getTerminalSize()
	initScreen()
	startKeyHandler()
	getSearch()

print(YtVideo("UCS1_W-xMyg").title)
