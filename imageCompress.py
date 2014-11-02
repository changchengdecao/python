#!/usr/bin/python
#Filename image_compress.py

import os
import sys
import Image
import time

def resize(imgPath,width=700):
	allowImageType = ['jpg','jpeg','gif','png']
	if imgPath.split('.')[-1].lower() in allowImageType :
		img = Image.open(imgPath)
		(w,h) = img.size
		if w>width:
			try:
				height = h * width / w
				out = img.resize((width,height),Image.ANTIALIAS)
				out.save(imgPath,quality=95)
			except IOError,e:
				print "error:",e


imageFolder = "./"
count = 0
time.clock()
for path, dirs, files in os.walk(imageFolder):
	for itme in files:
		imgPath = path+"/"+itme
		if os.path.isfile(imgPath):
			count = count +1
			#print imgPath
			resize(imgPath)

print "count:",count,",time:",time.clock(),"s"
