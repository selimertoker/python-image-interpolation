from PIL import Image
from progress import progressBar

img1path=input("input image: ")
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
        try:
            pxlS[2*x+1, 2*y] = (int((pxl1[x, y][0]/2)+(pxl1[x+1, y][0]/2)), int((pxl1[x, y][1]/2)+(pxl1[x+1, y][1]/2)), int((pxl1[x, y][2]/2)+(pxl1[x+1, y][2]/2)))
        except:
            pxlS[2*x+1, 2*y] = pxlS[2*x, 2*y]
    progressBar(y/2, h1, "Y:"+str(y), "processing...")

for y in range(h1):
    for x in range(w1):
        try:
            pxlS[2*x, 2*y+1] = (int((pxlS[2*x, 2*y][0]/2)+(pxlS[2*x, 2*y+2][0]/2)), int((pxlS[2*x, 2*y][1]/2)+(pxlS[2*x, 2*y+2][1]/2)), int((pxlS[2*x, 2*y][2]/2)+(pxlS[2*x, 2*y+2][2]/2)))
            pxlS[2*x+1, 2*y+1] = (int((pxlS[2*x+1, 2*y][0]/2)+(pxlS[2*x+1, 2*y+2][0]/2)), int((pxlS[2*x+1, 2*y][1]/2)+(pxlS[2*x+1, 2*y+2][1]/2)), int((pxlS[2*x+1, 2*y][2]/2)+(pxlS[2*x+1, 2*y+2][2]/2)))
        except:
            pxlS[2*x, 2*y+1] = pxlS[2*x, 2*y]
            pxlS[2*x+1, 2*y+1] = pxlS[2*x+1, 2*y]
    progressBar(h1/2+y/2+1, h1, "Y:"+str(y), "processing...")

imgS.save(imgSpath)
