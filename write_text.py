from PIL import Image, ImageDraw, ImageFont
#https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
def image_writer(inFile, textToWrite, outFile):
    img = Image.open(inFile)
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('ttf/OpenSans-Regular.ttf', 40)
    d1.text((0, 0), textToWrite, font=myFont, fill =(255, 0, 0))
    img.show()
    img.save(outFile)
