'''Script para modificar tamaño y extensión de varios archivos en la carpeta donde se ejecuta'''
from PIL import Image
import os, sys

basewidth = 512
i = 0

for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
	if filename.endswith(".jpg"):
		img = Image.open(filename)
		wpercent = (basewidth/float(img.size[0]))
		hsize = int((float(img.size[1])*float(wpercent)))
		img = img.resize((basewidth,hsize), Image.ANTIALIAS)
		img.save(str(i)+'.png') 
		os.remove(filename)
		i += 1