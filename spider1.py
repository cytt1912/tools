import urllib.request
url = "http://www.baidu.com"
reponse = urllib.request.urlopen(url=url)
print(reponse.read().decode())

