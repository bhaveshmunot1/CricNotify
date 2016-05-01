import os

def Notify(title, message):
	os.system('notify-send ' + '"' + title + '"' + ' ' + '"' + message + '"')

Notify('Title', 'This is a message!')