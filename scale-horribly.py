from PIL import Image
from progress import progressBar

img1path=input("image 1: ")
imgSpath=input("save image to: ")

img1 = Image.open(img1path)
pxl1 = img1.load()
w1, h1 = img1.size

print("w:", w1, "h:", h1)

imgS = Image.new("RGB", (2*w1, 2*h1), color = 0)
pxlS = imgS.load()

for y in range(h1):
    for x in range(w1):
        pxlS[2*x, 2*y] = pxl1[x, y]
    progressBar(y, h1, "Y:"+str(y), "processing...")

imgS.save(imgSpath)
