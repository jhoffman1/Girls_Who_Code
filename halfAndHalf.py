from PIL import Image

## FUNCTIONS

def negative(pixel):
   #find the red, green, and blue values
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    #find the new red, green, and blue values
    newRed = 255 - red
    newGreen = 255- green
    newBlue = 255-blue

    #create new pixel
    p = (newRed,newGreen,newBlue)

    #add pixel to new pixel list
    newPixelList.append(p)

def overExpose(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    newRed = red*2
    if newRed > 255:
        newRed = 255

    newGreen = green*2
    if newGreen > 255:
        newGreen = 255

    newBlue = blue*2
    if newBlue > 255:
        newBlue = 255

    p = (newRed,newGreen,newBlue)

    #add pixel to new pixel list
    newPixelList.append(p)

##RUNNING CODE
#Import the image and make pixel list
myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

counter = 0
length = len(pixelList)
halfWay = length//2

#pixel manipulation
for pixel in pixelList:
    if (counter <= halfWay):
        overExpose(pixel)
    else:
        negative(pixel)
        
    counter = counter+1
    
    

#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
#newImage.save("newPhoto.jpg","jpg")
