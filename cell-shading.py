##### This program takes a stock and image and converts it to a cell shaded version of its self in order to
##### better define the areas paint would be applied.

import os
import cv2
import numpy as np
################# VARIABLES #######################
png_array = []
jpg_array = []
choice = []
location = "photofolder here"
files = os.listdir(r'C:\')  # need the r to avoid changing
# to forward slash
###################################################
### OPENING A FILES LOCATION

for ii in files:  # seperating pgn and jpg images, not sure why, but definately the images need to be sorted out.
    name = ii
    if (name[-4:]) == '.JPG':
        jpg_array.append(name)
    elif (name[-4:]) == '.PNG':
        png_array.append(name)
photo_array = png_array + jpg_array

# Choose the file name.
while not choice:
    print("Available files : " "\n", photo_array)
    choice = input("Type exact case and extension .... ")

    if choice in photo_array:
        continue
    else:
        choice = []
        print('There is an error in you selection, please select again.')

location = location + choice

############# OPENING AN IMAGE
img = cv2.imread(location, -1)  # -1 is colour neglecting transparency

### BLURING AN IMAGE
img = cv2.GaussianBlur(img, (5,5), 0)
img = cv2.medianBlur(img, 5)

#cv2.imshow('tea kettle', img) # TESTING DISPLAY ONLY
#cv2.waitKey(0)

##### convert the image to hsv colour
hsvimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#print(hsvimg)
#cv2.imshow('hsvtk', hsvimg) # TESTING DISPLAY ONLY
#cv2.waitKey(0)

## ROUNDING OUT THE brightness level
for iii in hsvimg:
   for ii in iii:
       ii[2] = round(ii[2]/30)*30 ### it takes the v value of the picture and rounds it to the nearest 30.
hsvimg = cv2.GaussianBlur(hsvimg, (5,5), 0)
hsvimg = cv2.medianBlur(hsvimg, 5)

#colour = hsvimg[300:400,250:350] # testing a section of image
#print(colour)
#colour = cv2.cvtColor(colour, cv2.COLOR_HSV2BGR)
#cv2.imshow('test', colour)

cell = cv2.cvtColor(hsvimg, cv2.COLOR_HSV2BGR)
cv2.imshow('altered hsv', cell)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print(colour)

###### to save ######
#os.chdir(r'C:\')
#cv2.imwrite('Cell_Shaded_'+str(choice), cell)















