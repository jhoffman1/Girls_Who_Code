from PIL import Image

def intensityCalculator(pixel):
	r = pixel[0]
	g = pixel[1]
	b = pixel[2]
	return r+g+b


# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

# Import image.
my_image = Image.open("brooklyn.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata()
image_list = list(image_list) #THis will hold a list of 

recolored = [] #list holding the pixel data for the new image.

for each in image_list:
	intensity = intensityCalculator(each)

	if intensity < 182:
		c = (0,51,76)
	elif intensity >= 182 and intensity < 364:
		c = (217,26,33)
	elif intensity >= 364 and intensity < 546:
		c = (112,150,158)
	else:
		c = (252,227,166)
	recolored.append(c)

#check for intensity and color the pixel in recolored based on intensity. 
#A pixel's "intensity" will be higher if the value of Red Green and Blue added together is higher.
#Good numbers to start with for intensity - 182, 364, 546 - but your numbers may vary
#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.



# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size)
new_image.putdata(recolored)
new_image.show()
new_image.save("recolored.jpg", "jpeg")


