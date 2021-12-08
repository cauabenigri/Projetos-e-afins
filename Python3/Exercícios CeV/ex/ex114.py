import urllib.request

if urllib.request.urlopen('http://pudim.com.br').getcode() == 200:
    print()