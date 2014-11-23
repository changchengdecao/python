import os

for path,dirs,files in os.walk("./image"):
	for items in files:
		name = items[-7:-5]+".jpg"
		#print name
		#print path
		os.rename(path+"/"+items,path+"/"+name)
