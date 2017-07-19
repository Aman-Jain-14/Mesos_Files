import urllib
import json
import time

link = "http://127.0.0.1:5050/metrics/snapshot"
f = urllib.urlopen(link)

while(f):
	f = urllib.urlopen(link)
	myfile = f.read()
	j = json.loads(myfile)
	print j['allocator/mesos/resources/mem/offered_or_allocated']
	time.sleep(1)