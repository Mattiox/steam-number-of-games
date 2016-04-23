#!/usr/bin/env python
import urllib2
import time

urltotal='http://store.steampowered.com/search/results?sort_by=_ASC&category1=998&page=1&snr=1_7_7_230_7'
urllinux='http://store.steampowered.com/search/results?sort_by=_ASC&category1=998&os=linux&page=1&snr=1_7_7_230_7'

finder='showing 1 - 25 of '

response = urllib2.urlopen(urltotal)
page = response.read()

for line in page.split("\n"):
	if finder in line:
		line = line[22:-10]
		totalgames = line
		break

response = urllib2.urlopen(urllinux)
page = response.read()

for line in page.split("\n"):
	if finder in line:
		line = line[22:-10]
		linuxgames = line
		break

print("Total Games: " + totalgames)
print("Linux Games: " + linuxgames)
linuxpercentage = float(linuxgames)  * 100 / float(totalgames)
print("Linux Percentage: " + str(linuxpercentage))

with open("log.txt", "a") as f:
    f.write(time.strftime("%d/%m/%Y") + " " + totalgames + " " + linuxgames + " " + str(linuxpercentage) + "\n")
