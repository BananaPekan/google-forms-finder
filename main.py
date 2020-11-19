import string
import random
import requests
import sys
from colorama import init, AnsiToWin32, Fore
import threading

# Made with ♥ by GamerStop#0069

def thread(new, args=[]):
	if args == []:
		threading.Thread(target=new).start()
	else:
		threading.Thread(target=new, args=args).start()

proxy_server = 'ip:port'

proxy = {
	'https://httpbin.org/ip' : '208.80.28.208:8080'
}


init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream

threads = 0

def check():
	global threads
	found = open('valid.txt', 'a')
	genform = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase , k = N)) 
	formlink = "https://forms.gle/" + str(genform)
	r = requests.get(formlink, proxies=proxy)
	if r.status_code == 404:
		print(Fore.RED + 'invalid link  ' + str(r.status_code) +  '  ' + formlink + '\n', file=stream)
	elif r.status_code == 200:
		print(Fore.GREEN + 'link working  ' + str(r.status_code) +  '  ' + formlink + '\n', file=stream)
		valid = str(formlink) + '\n'
		found.write(valid)
	else:
		print(r.status_code)
	found.close()
	threads -= 1

N = 17

max_threads = int(input('How many max threads you want??'))


loops = int(input('How many loops you want?'))
for i in range(loops):
	if threads < max_threads:
		thread(check)
		threads += 1
	else:
		while True:
			if threads < max_threads:
				thread(check)
				threads += 1
				break
			else:
				pass
