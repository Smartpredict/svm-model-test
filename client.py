import requests
from PIL import Image
import numpy as np

#Changer le chemain pout tester d'autre image

img = Image.open('./imagesTest/test.tif').convert('L')


datainv = list(img.getdata())
dataimg = [0]*784

i = 0
for pixel in datainv:
    pixel = (255-pixel)/255.0
    dataimg[i] = pixel
    i = i+1

print(dataimg)
payload = {"imdata": dataimg}

r = requests.post('http://127.0.0.1:5000/predict', json = payload)

print(r.text)
