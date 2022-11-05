from PIL import Image
from progress import progressBar

img1path=input("image 1: ")
img2path=input("image 2: ")
imgSpath=input("save image to: ")

h3 = int()
w3 = int()
img1 = Image.open(img1path)
img2 = Image.open(img2path)
pxl1 = img1.load()
pxl2 = img2.load()
w1, h1 = img1.size
w2, h2 = img2.size

if (h1 <=  h2): h3 = h1
else: h3 = h2

if (w1 <=  w2): w3 = w1
else: w3 = w2

print("w:", w1, w2, w3, "h", h1, h2, h3)

imgS = Image.new("RGB", (w3, h3), color = 0)
pxlS = imgS.load()

for y in range(h3):
    for x in range(w3):
        pxlS[x, y] = ((int(pxl1[x, y][0]/2)+int(pxl2[x, y][0]/2)), (int(pxl1[x, y][1]/2)+int(pxl2[x, y][1]/2)), (int(pxl1[x, y][2]/2)+int(pxl2[x, y][2]/2)))
    progressBar(y, h3, "Y:"+str(y), "processing...")

imgS.save(imgSpath)
