import string
import random
import requests
import sys
from colorama import init, AnsiToWin32, Fore

# Made with ♥ by GamerStop#0069

proxy_server = 'ip:port'

proxy = {
	'https://httpbin.org/ip' : '208.80.28.208:8080'
}


init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream


N = 17


times = 1000
for i in range(times):
	genform = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase , k = N)) 
	formlink = "https://forms.gle/" + str(genform)
	r = requests.get(formlink, proxies=proxy)
	if r.status_code == 404:
		print(Fore.RED + 'invalid link  ' + str(r.status_code) +  '  ' + formlink, file=stream)
	elif r.status_code == 200:
		print(Fore.GREEN + 'link working  ' + str(r.status_code) +  '  ' + formlink, file=stream)
	else:
		print(r.status_code)
