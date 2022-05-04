import sys
import requests


def aaa(value):
    r = requests.get('http://192.168.11.129/index/', cookies={'autogeneratoridhaha': value})
    print(r.text)
    
    
aaa(sys.argv[1])