# encoding:utf-8
#! section17.py - image process demo
from PIL import ImageColor,Image
def getColorValue():
    print(ImageColor.getcolor('red','RGBA'))

def openImage():
    starIm=Image.open('D:\\4.png')
    print("Size:"+str(starIm.size))
    print("File name:"+starIm.filename)
    print("Format:"+starIm.format+" /Format Description:"+starIm.format_description)

def createNewImage():
    im = Image.new('RGBA',(100,200),'purple')
    im.save('D:\\purple.png')
    
def cropImage():
    starIm=Image.open('D:\\4.png')
    newim=starIm.crop((13,7,96,102))
    newim.save('D:\\newstar.png')

def pastedImg():
    jellyfish=Image.open('C:\\Users\\Public\\Pictures\\Sample Pictures\\Jellyfish.jpg')
    originImg=jellyfish.copy()
    star=Image.open('D:\\newstar.png')
    originImg.paste(star,(0,0))
    originImg.paste(star,(400,500))
    originImg.save('D:\\jellyfish.jpg')

#getColorValue()
#openImage()
#createNewImage()
#cropImage()
pastedImg()