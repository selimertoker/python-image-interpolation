from PIL import Image
from progress import progressBar

img1path=input("image 1: ")
imgSpath=input("save image to : ")

patt = (0.25, -0.5, 0.25, -0.5, 1, -0.5, 0.25, -0.5, 0.25)
div = len(patt)

img1 = Image.open(img1path)
pxl1 = img1.load()
w1, h1 = img1.size

print("w:", w1, "h:", h1)

imgS = Image.new("RGB", (w1, h1), color = 0)
pxlS = imgS.load()

for y in range(h1):
    for x in range(w1):
        try:
            Rval = (patt[0]*pxl1[x-1, y-1][0])+(patt[1]*pxl1[x, y-1][0])+(patt[2]*pxl1[x+1, y-1][0])+(patt[3]*pxl1[x-1, y][0])+(patt[4]*pxl1[x, y][0])+(patt[5]*pxl1[x+1, y][0])+(patt[6]*pxl1[x-1, y+1][0])+(patt[7]*pxl1[x, y+1][0])+(patt[8]*pxl1[x+1, y+1][0])
            Gval = (patt[0]*pxl1[x-1, y-1][1])+(patt[1]*pxl1[x, y-1][1])+(patt[2]*pxl1[x+1, y-1][1])+(patt[3]*pxl1[x-1, y][1])+(patt[4]*pxl1[x, y][1])+(patt[5]*pxl1[x+1, y][1])+(patt[6]*pxl1[x-1, y+1][1])+(patt[7]*pxl1[x, y+1][1])+(patt[8]*pxl1[x+1, y+1][1])
            Bval = (patt[0]*pxl1[x-1, y-1][2])+(patt[1]*pxl1[x, y-1][2])+(patt[2]*pxl1[x+1, y-1][2])+(patt[3]*pxl1[x-1, y][2])+(patt[4]*pxl1[x, y][2])+(patt[5]*pxl1[x+1, y][2])+(patt[6]*pxl1[x-1, y+1][2])+(patt[7]*pxl1[x, y+1][2])+(patt[8]*pxl1[x+1, y+1][2])

            pxlS[x, y] = (int(Rval*div), int(Gval*div), int(Bval*div))
        except:
            pxlS[x, y] = (255, 0, 255)
    progressBar(y, h1, "Y:"+str(y), "processing...")

imgS.save(imgSpath)
