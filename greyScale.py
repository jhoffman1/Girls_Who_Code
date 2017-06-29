from PIL import Image

#Import the image and make pixel list
myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

#pixel manipulation
for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]


    #find average of color values
    average = ((red + green + blue) // 3)


    #create new pixel
    newRed = average
    newGreen = average
    newBlue = average

    p = (newRed,newGreen,newBlue)
    #p = (average,average,average)
    

    #add pixel to new pixel list
    newPixelList.append(p)

#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
#newImage.save("newPhoto.jpeg","jpeg")
