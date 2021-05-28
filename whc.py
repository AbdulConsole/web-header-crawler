import os
import urllib3
import sys
import http
import json

print("\033[92m")
os.system("figlet  Web Header Crawler")
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
print("\n ================+================ \n")
print("status code: ",r.status)
print("\n ================+================ \n")
print(str(r.headers))
