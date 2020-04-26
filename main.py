import requests
from colorama import init, Fore, Back, Style
from datetime import datetime
import time

init(convert=True)


def single():
	link = input("Enter product link: ")
	q = int(input("# of views: "))

	print(Fore.GREEN, "Running...")

	for i in range(q):
		print(Fore.CYAN, "[{}]  Task [{}]  ".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i), end=' ')
		try:
			r = requests.get(link)
			print(Fore.GREEN, "View Added")
		except:
			print(Fore.RED, "Request Failed")
			time.sleep(1)


def list_():
	print(Fore.YELLOW, "Make sure your links are loaded in links.txt")
	print("Running too many tasks without proxies can result in a soft ban")
	links = []
	with open('links.txt', 'r') as f:
		links = [line.strip() for line in f]

	q = int(input("# of views per link: "))

	for i in range(len(links)):
		print(Fore.YELLOW, "[{}]  Starting Link [{}]  ".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i))
		for j in range(q):
			print(Fore.CYAN, "[{}]  Task [{}]  ".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), j), end=' ')
			try:
				r = requests.get(links[i])
				print(Fore.GREEN, "View Added")
			except:
				print(Fore.RED, "Request Failed")
				time.sleep(1)

if __name__ == "__main__":
	print("[1] Link Mode")
	print("[2] List Mode")
	c = int(input("Select Mode:"))
	if(c == 1):
		single()
	if(c == 2):
		list_()
