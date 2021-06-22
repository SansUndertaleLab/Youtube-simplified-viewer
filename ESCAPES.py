# huge thanks to this: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
import FUNC as f

class EscapeStarters: #characters that start a escape code
	argStarter="[" #starts the command value

	ctrl="^[" #doesnt actually work, idk why
	octal="\033"+argStarter
	unicode="\u001b"+argStarter
	hexadecimal="\x1b"+argStarter
	decimal="27"+argStarter #this also doesnt work...

def buildEscape(theType,theValue):
	if theType=="hex" or theType=="hexadecimal":
		if theValue.startswith("0x"):
			theValue=f.withoutFirst(f.withoutFirst(theValue))
		return EscapeStarters.hexadecimal+theValue
	elif theType=="octal" or theType=="oct":
		return EscapeStarters.octal+theValue
	elif theType=="unicode":
		return EscapeStarters.unicode+theValue
	elif theType=="esc" or theType=="escape":
		return EscapeStarters.hexadecimal+theValue

def newlinelessPrint(string):
	print(string, end='')
	from sys import stdout
	stdout.flush()

class Escapes:
	bell="\a" #makes terminal ring
	backspace="\b" #deletes character behind where it is printed (if the character is on the same line)

	loadScreen=buildEscape("esc","?47l") #save current screen
	saveScreen=buildEscape("esc","?47h") #load previously saved screen

	class Tabs:
		vertical="\v" #wierd tab
		horizontal="\t" #normal tab used when programming

	newline="\n" #makes new line
	formfeed="\f" #form feed, or new page
	carraigeReturn="\r" #part of windows newline
	esc=buildEscape("hex","0x1B") #escape key
	delete=buildEscape("hex","0x7F") #delete key, not sure what it does but it does something

	class Cursor:
		makeInvisible=buildEscape("esc","?25l") #hide cursor
		makeVisible=buildEscape("esc","?25h") #show cursor

		home=buildEscape("esc","H") #move cursor to home (0,0)
		moveTo="row;columnH" #template for a moveTo escape char
	
		def moveEscape(row,column):
			return buildEscape("esc",
				"row;columnH".replace("row",str(row))
							 .replace("column",str(column))
				)
	
		save=buildEscape("esc","s") #save current cursor position
		load=buildEscape("esc","u") #load from save
	
		up="#A" #moves up # lines
		def upEscape(n): #generate escape to move up
			return buildEscape("esc","#A".replace("#",str(n)))
		
		up="#B" #moves down # lines
		def downEscape(n): #generate escape to move down
			return buildEscape("esc","#B".replace("#",str(n)))
		
		downAndStart="#E"
		def downAndStartEscape(n): #generate escape to move down and start of line
			return buildEscape("esc","#E".replace("#",str(n)))
		
		upAndStart="#F"
		def upAndStartEscape(n): #generate escape to move up and start of line
			return buildEscape("esc","#F".replace("#",str(n)))

		right="#C" #moves right # lines
		def rightEscape(n): #generate escape to move right
			return buildEscape("esc","#C".replace("#",str(n)))
				
		left="#D" #moves left # lines
		def leftEscape(n): #generate escape to move left
			return buildEscape("esc","#D".replace("#",str(n)))
		
		column="#G" #move to column #
		def moveToColumn(n):
				return buildEscape("esc","#G".replace("#",str(n)))

	class Erase:
		screen=buildEscape("esc","J") #clear the screen
		scrollbackScreen=buildEscape("esc","2J") #clear entire screen, might not work properly if cursor not at (0,0), as it uses newlines!
		scrollback=buildEscape("esc","3J") #discovered this
	
		line=buildEscape("esc","K") #erase line cursor is on
		entireLine=buildEscape("esc","2K")
	
		class FromCursor:
			toEndOfScreen=buildEscape("esc","0J") #clear from cursor to end of the screen
			toStartOfScreen=buildEscape("esc","1J") #clear from cursor to start of screen
	
			toStartOfLine=buildEscape("esc","1K") #clear from cursor to start of line
			toEndOfLine=buildEscape("esc","0K") #clear from cursor to end of line
	
	class Style: #change text shape
		reset=buildEscape("esc","0m") #resets all style (color and format)
		bold=buildEscape("esc","1m") #bold all text after
		dim=buildEscape("esc","2m") #dim all text after
		italic=buildEscape("esc","3m") #italic all text after
		underline=buildEscape("esc","4m") #underline all text after
		blink=buildEscape("esc","5m") #make all text after blink
		#6 does nothing
		invert=buildEscape("esc","7m") #invert all colors after
		invisible=buildEscape("esc","8m") #make all text after invisible
		strikethrough=buildEscape("esc","9m") #make all text after strikethrough. does not work on terminal.app 

	class Color8: #print bold before for bright color,
		#print dim before for dim color
		class Foreground:
			black=buildEscape("esc","30m")
			red=buildEscape("esc","31m")
			green=buildEscape("esc","32m")
			yellow=buildEscape("esc","33m")
			blue=buildEscape("esc","34m")
			magenta=buildEscape("esc","35m")
			cyan=buildEscape("esc","36m")
			white=buildEscape("esc","37m")
		class Background:
			black=buildEscape("esc","40m")
			red=buildEscape("esc","41m")
			green=buildEscape("esc","42m")
			yellow=buildEscape("esc","43m")
			blue=buildEscape("esc","44m")
			magenta=buildEscape("esc","45m")
			cyan=buildEscape("esc","46m")
			white=buildEscape("esc","47m")
	class Color256:
		class Foreground:
			template="38;5;$#m" # # is the color id
			def color(n):
				return buildEscape("esc","38;5;#m".replace("#",str(n)))
		class Background:
			template="48;5;$#m" # # is the color id
			def color(n):
				return buildEscape("esc","48;5;#m".replace("#",str(n)))
	class TrueColor:
		class Foreground:
			template="38;2;r;g;bm"
			def color(r,g,b):
				return buildEscape("esc","38;2;r;g;bm".replace("r",str(r)).replace("g",str(g)).replace("b",str(b)))
		class Background:
			template="48;2;r;g;bm"
			def color(r,g,b):
				return buildEscape("esc","48;2;r;g;bm".replace("r",str(r)).replace("g",str(g)).replace("b",str(b)))
