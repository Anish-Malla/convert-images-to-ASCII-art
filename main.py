import cv2
import numpy as np

# setup
IMAGE_PATH = 'goldengate.jpg'
image = cv2.imread(IMAGE_PATH)
image = cv2.resize(image,(100, 100), interpolation=cv2.INTER_AREA)

brightness = np.empty((image.shape[0], image.shape[1]))
ascii_image = [] 

#Caclulate brightness values
for x in range(len(image)):
    for y in range(len(image[x])):
        pixel = image[x][y]
        avg = (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) // 3
        brightness[x][y] = avg

#Brightness to Ascii Values
ascii_vals = [' ', '`','^','"',',',':',';','I','l','!','i','~','+','_','-','?',']',
        '[','}','{','1',')','(','|','/','t','f','j','r','x','n','u','v','c','z',
        'X','Y','U','J','C','L','Q','0','O','Z','m','w','q','p','d','b','k','h',
        'a','o','*','#','M','W','&','8','%','B','@','$']

ascii_vals_brightness = {}
val = 0
increment = 255 // len(ascii_vals)

for x in ascii_vals:
    ascii_vals_brightness[(val, val + increment)] = x
    val += increment + 1

# assigning values
for x in range(len(brightness)):
    temp = []
    for y in range(len(brightness[x])):
        val = brightness[x][y]
        for low, high in ascii_vals_brightness.keys():
            if val >= low and val <= high:
                temp.append(ascii_vals_brightness[(low, high)])
                break
    ascii_image.append(temp)

#Printing it out!
for row in ascii_image:
    line = [x+x+x for x in row]
    print("".join(line))
