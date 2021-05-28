import os
import urllib3
import sys
import http
from time import sleep

def clear(): 
    _ = os.system('clear' if os.name =='posix' else 'cls')
sleep(2)
clear()
print("\033[92m")
#os.system("figlet  WebHC Header Crawler")
print('''\t _      __    __   __ _______
\t| | /| / /__ / /  / // / ___/
\t| |/ |/ / -_) _ \/ _  / /__ header
\t|__/|__/\__/_.__/_//_/\___/crawler
''')
print("\033[91m")
print("              created by AbdulConsole")
print("\033[93m")
url = input("Enter website link: \033[92m")
url.rstrip()

print('''
======================================
         {0}
======================================
'''.format(url))
http.client.HTTPConnection.debuglevel=5
http = urllib3.PoolManager()
r = http.request('GET',url)

print("\033[94m")
print("========== status code: ",r.status, " ===========")
print("\033[92m")
print(str(r.headers))