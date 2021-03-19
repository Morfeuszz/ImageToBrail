from PIL import Image
import PIL.ImageOps 
import numpy
import sys
import cv2
import os, os.path

brail = {
    "" : "⠁",
  	1 : "⠁",
    12 : "⠉",
    123 : "⠋",
    1234 : "⠛",
    12345 :  "⠟",
    123456 : "⠿",
    12346 : "⠻",
    1235 : "⠏",
    12356 : "⠯",
    1236 : "⠫",
    124 : "⠙",
    1245 : "⠝",
    12456 : "⠽",
    1246 : "⠹",
    125 : "⠍",
    1256 : "⠭",
    126 : "⠩",
    14 : "⠑",
    145 : "⠕",
    146 : "⠱",
    15 : "⠅",
    156 : "⠥",
    13 : "⠃",
    135 : "⠇",
    1356 : "⠧",
    136 : "⠣",
    134 : "	⠓",
    1345 : "⠗",
    1346 : "⠳",
    13456 : "⠷",
    14 : "⠉",
    145 : "⠙",
    1456 : "⠵",
    15 : "⠑",
    16 : "⠡",
  	2 : "⠈",
    23 :  "⠊",
    235 : "⠎",
    236 : "⠪",
    234 : "⠚",
    2345 :  "⠞",
    2346 : "⠺",
    23456 : "⠾",
    2356 : "⠮",
    24 : "⠘",
    245 : "⠜",
    246 : "⠸",
    2456 : "⠼",
    25 : "⠌",
    256 : "⠬",
    26 : "⠨",
    3 :  "⠂",
    34 :  "⠒",
    345 : "⠖",
    346 : "⠲",
    3456 : "⠶",
    35 : "⠆",
    356 : "⠦",
    36 : "⠢",
    4 : "⠐",
    45 : "⠔",
    456 : "⠴",
    46 : "⠰",
    5 : "⠄",
    56 : "⠤",
    6 : "⠠"
}

"""DIR = 'frames'
print (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

vidcap = cv2.VideoCapture('badapple.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frames/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  #print('Read a new frame: ', success)
  count += 1

"""

img = Image.open(yourimagename)

if img.mode == 'RGBA':
    r,g,b,a = img.split()
    rgb_image = Image.merge('RGB', (r,g,b))
    inverted_image = PIL.ImageOps.invert(rgb_image)

    inverted_image = rgb_image

    rgb_image.save('new_name2.png')

else:
    inverted_image = PIL.ImageOps.invert(img)

    inverted_image = img

    inverted_image.save('new_name.png')


def myround(x, base=5):
    return base * round(x/base)


width, height = inverted_image.size
inverted_image = inverted_image.resize((myround(width,2),myround(height,3)))



thresh = 20
fn = lambda x : 255 if x > thresh else 0
r = inverted_image.convert('L').point(fn, mode='1')
r.save('foo.png')   

pix = r.load()
'''
imgArray = []
tempArray = []
tempArray2 = []
for y in range(int(myround(height,3)/3)):
    for x in range(int(myround(width,2)/2)):
        for yi in range(3):
            for xi in range(2):
                tempArray2.append(pix[xi + (x * 2),yi + (y * 3)])
        tempArray.append(tempArray2)
        tempArray2 = []
    imgArray.append(tempArray)
    tempArray = []
'''
imgArray = []
tempArray = []
tempString = ""
for y in range(int(myround(height,3)/3)):
    for x in range(int(myround(width,2)/2)):
        for yi in range(3):
            for xi in range(2):
                if pix[xi + (x * 2),yi + (y * 3)] == 0:
                    tempString += str((yi * 2) + xi + 1)
        tempArray.append(tempString)
        tempString = ""
    imgArray.append(tempArray)
    tempArray = []


brailArray = []
tempArray2 = []
for x in imgArray:
    for y in x:
        if y != "":
            tempArray2.append(brail[int(y)])
        else:
            tempArray2.append(brail[y])
    brailArray.append(tempArray2)
    tempArray2 = []

resultTemp = ""

sys.stdout = open("test.txt", "w",encoding='utf-8', errors='ignore')
for row in brailArray:
    for char in row:
        resultTemp += char
    print(resultTemp)
    resultTemp = ""


sys.stdout.close()
