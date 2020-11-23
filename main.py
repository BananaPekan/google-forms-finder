from colorama import init, AnsiToWin32, Fore
import threading
import requests
import string
import random
import sys

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

printfix = []
alreadyFound = []

init(convert=True)

threads = 0

def check():
    global threads
    genform = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase , k = N))
    formlink = "https://forms.gle/" + str(genform)
    if formlink in alreadyFound:
        while True:
            formlink = "https://forms.gle/" + str(genform)
            if formlink in alreadyFound:
                pass
            else:
                alreadyFound.append(formlink)
                r = requests.get(formlink, proxies=proxy)
                if r.status_code == 404:
                    printfix.append('invalid link  ' + str(r.status_code) +  '  ' + formlink)
                elif r.status_code == 200:
                    printfix.append('link working  ' + str(r.status_code) +  '  ' + formlink)
                    valid = str(formlink) + '\n'
                    found = open('valid.txt', 'a')
                    found.write(valid)
                    found.close()
                else:
                    print(r.status_code)
                break
    else:
        alreadyFound.append(formlink)
        r = requests.get(formlink, proxies=proxy)
        if r.status_code == 404:
            printfix.append('invalid link  ' + str(r.status_code) +  '  ' + formlink)
        elif r.status_code == 200:
            printfix.append('link working  ' + str(r.status_code) +  '  ' + formlink)
            valid = str(formlink) + '\n'
            found = open('valid.txt', 'a')
            found.write(valid)
            found.close()
        else:
            print(r.status_code)
    threads -= 1

N = 17



max_threads = int(input('How many threads do you want? '))
loops = int(input('How many loops do you want? '))

loopsLeft = loops

def printResults():
    global printfix, loopsLeft
    while True:
        if loopsLeft <= 0:
            break
        elif len(printfix) <= 0:
            pass
        else:
            for result in printfix:
                if result.startswith('invalid'):
                    print(Fore.LIGHTRED_EX + result + Fore.RESET)
                else:
                    print(Fore.LIGHTGREEN_EX + result + Fore.RESET)
                printfix.remove(result)

thread(printResults)

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
    loopsLeft -= 1
