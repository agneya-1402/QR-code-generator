import pyqrcode

url=pyqrcode.create("https://www.google.com/")
url.svg("uca-url.svg",scale=3)
a=url.terminal(quiet_zone=1)
print(a)