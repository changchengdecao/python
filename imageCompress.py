#!/usr/bin/python
#Filename imageCompress.py

import os
import sys
import Image

def resize(imgPath,width=700):
	allowImageType = ['jpg','jpeg','gif','png']
	if os.path.isfile(imgPath) and imgPath.split('.')[-1].lower() in allowImageType :
		img = Image.open(imgPath)
		(w,h) = img.size
		if w>width:
			height = h * width / w
			out = img.resize((width,height),Image.ANTIALIAS)
			out.save(imgPath,quality=95)


imageFolder = "./"
for path, dirs, files in os.walk(imageFolder):
	for itme in files:
		imgPath = path+itme
		resize(imgPath)
