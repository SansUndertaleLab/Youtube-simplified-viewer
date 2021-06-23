## YtVideo class
```python
import FUNC as f
import re

class YtVideo:
	def __init__(self,linkOrId):
		if linkOrId.startswith("http"):
			self.id=re.findall(r"watch\?v=(\S{11})",linkOrId)[0]
		else:
			self.id=linkOrId
		self.link="https://www.youtube.com/watch?v="+self.id
		self.page=f.callWeb(self.link)
		self.title=self.page\
					  .replace("<title>","ǉ")\
					  .replace("</title>","ǉ")\
					  .split("ǉ")[1]\
					  .strip(" - YouTube")
		self.author=re.findall(r"(?<=\"author\":\")[A-Z a-z]+(?=\")",self.page)[0]
		self.views=re.findall(r"(?<=\"viewCount\":\")[0-9, ]+(?=\")",self.page)[0]
		self.likes=re.findall(r"(?<=\"defaultIcon\":{\"iconType\":\"LIKE\"},\"defaultText\":{\"accessibility\":{\"accessibilityData\":{\"label\":\")[0-9,]+",self.page)[0]
		self.dislikes=re.findall(r"(?<=\"defaultIcon\":{\"iconType\":\"DISLIKE\"},\"defaultText\":{\"accessibility\":{\"accessibilityData\":{\"label\":\")[0-9,]+",self.page)[0]
	def open(self):
		webbrowser.open(self.link)
	def __str__(self):
		return "id: {}\n    title: {}\n    author: {}    \n    views: {}\n    likes: {}\n    dislikes: {}\n    link: {}"\
					.format(self.id,self.title,self.author,self.views,self.likes,self.dislikes,self.link)
```
## docs
- ***obj*** `YtVideo(linkOrId)`:  
  ***arg*** `linkOrId`: a link to a yt video or id
  - ***str*** `id`: the video's id
  - ***str*** `link`: the video's link
  - ***str*** `page`: the contents of the video's youtube page
  - ***str*** `title`: the video's title
  - ***str*** `author`: the name of the channel that made the video
  - ***str*** `views`: the number of views
  - ***str*** `likes`: the number of likes
  - ***str*** `dislikes`: the number of dislikes
