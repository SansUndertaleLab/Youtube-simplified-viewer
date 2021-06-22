import webbrowser
import urllib.request
import re
searchlink = "https://www.youtube.com/results?search_query="
search=input().replace(" ","+")
searchlink = "https://www.youtube.com/results?search_query="+search
html = urllib.request.urlopen(searchlink)
videoIds = re.findall(r"watch\?v=(\S{11})",html.read().decode())
webbrowser.open("https://www.youtube.com/watch?v=" + videoIds[0])
