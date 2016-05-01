import os
import requests
from time import sleep
import pprint

def Notify(title, message):
	os.system('notify-send ' + '"' + str(title) + '"' + ' ' + '"' + str('\n' + message) + '"')

while True:
	res = requests.get("http://cricscore-api.appspot.com/csa")
	res = res.json()
	pp = pprint.PrettyPrinter(indent = 2)
	pp.pprint(res)
	match_id = input("Enter match ID: ")
	res = requests.get("http://cricscore-api.appspot.com/csa?id=" + str(match_id))
	res = res.json()
	Notify(res[0]['si'], res[0]['de'])
	sleep(30)
