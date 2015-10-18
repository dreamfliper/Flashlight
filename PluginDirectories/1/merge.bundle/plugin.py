# coding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def results(fields, original_query):
  from centered_text import centered_text
  application = fields['~application']
  return {
    "title": "Merge All '{0}' Windows".format(application),
    "run_args": [application],
	"html": centered_text(u"Merge All \"{0}\" Windows".format(application.capitalize())),
	"webview_transparent_background": True
  }

def run(applicationName):
	from applescript import asrun, asquote
	applicationName = applicationName.capitalize()
	ascript = '''
	tell application "''' + applicationName + '''"
      activate
    end tell
    delay 0.1 -- fix for termianl.app
	set location to (user locale of (get system info))
 	if location is equal to "zh_TW" then
 		tell application "System Events"
 			click menu item "合併所有視窗" of menu "視窗" of menu bar 1 of process "''' + applicationName + '''"
 		end tell
 	else
	    tell application "System Events"
		    click menu item "Merge All Windows" of menu "Window" of menu bar 1 of process "''' + applicationName + '''"
		end tell
	end if
	'''
	asrun(ascript.format(asquote(applicationName)))
