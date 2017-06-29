from PIL import Image

#Import the image and make pixel list
myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

#pixel manipulation
for pixel in pixelList:

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

#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
#newImage.save("newPhoto.jpg","jpg")
