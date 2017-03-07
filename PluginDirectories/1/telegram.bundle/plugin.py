# coding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("UTF-8")

def results(fields, original_query):
  from centered_text import centered_text
  name = fields['name']
  message = fields['~message']
  html='''
 	<html>
	<head>
	<style>
	html, body, #main {
	   width: 100%;
	   height: 100%;
	   margin: 0px;
	}
	#main {
	   display: table;
	}
	#main > div {
	   width: 100%;
	   display: table-cell;
	   text-align: center;
	   vertical-align: middle;
	}
	#letter {
	   display: inline-block;
	   width: 60%;
	   background-image: linear-gradient(#2270e7, #206de8);
	   color: white;
	   padding: 1em;
	   position: relative;
	   font-family: "HelveticaNeue", "Helvetica Neue";
	   border-radius: 8px;
	   text-align: left;
	}
	#body {
	   border-top: 1px solid #eee;
	   padding-top: 1em;
	}
	#body:empty {
	   display: none;
	}
	#recipients {
	   margin: top;
	}
	#recipients:before {
	   color: #eee;
	   content: "To: ";
	}
	</style>
	</head>
	<body>
	   <div id='main'>
	      <div>
	         <div id='letter'>
	            <p id='recipients'>name</p>
	            <p id='body'>message</p>
	         </div>
	      </div>
	   </div>
	</body>
	</html>
	'''#%(name,message)

  return {
    "title": "Telegram to  '{0}' with '{1}' ".format(name,message),
    "run_args": [fields],
	"html": html.replace('name',name).replace('message',message),
	"webview_transparent_background": True
  }

def run(fields):
	name = fields['name']
	message = fields['~message']

	from applescript import asrun, asquote
 	ascript = '''
	activate application "Telegram Desktop"
	tell application "System Events"
		click menu item "Show Telegram" of menu "Window" of menu bar 1 of process "Telegram"
		delay 0.3
		key code 53  --Esc
		set the clipboard to %s
		tell application "System Events" to keystroke "v" using command down
		key code 76	 --Enter
		delay 0.3
		set the clipboard to %s
		delay 0.3
		tell application "System Events" to keystroke "v" using command down
		key code 76  --Enter
	end tell
  	'''%(asquote(name),asquote(message))
  	asrun(ascript)