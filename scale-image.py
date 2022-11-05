from PIL import Image
from progress import progressBar

img1path=input("image 1: ")
imgSpath=input("save image to : ")

facx = int(input("x scaling: "))
facy = int(input("y scaling: "))
img1 = Image.open(img1path)
pxl1 = img1.load()
w1, h1 = img1.size

print("w:", w1, "h:", h1)

imgS = Image.new("RGB", (w1*facx, h1*facy), color = 0)
pxlS = imgS.load()

for y in range(h1):
    for yy in range(facy):
        for x in range(w1):
            for xx in range(facx):
                pxlS[xx+x*facx, yy+y*facy] = pxl1[x, y]
    progressBar(y, h1, "Y:"+str(y), "processing...")

imgS.save(imgSpath)
