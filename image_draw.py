import random
from PIL import Image, ImageDraw
import csv
import cv2 as cv
import os
from main import consumption
from main import per_hour1
import numpy as np
import operator
from functools import reduce

per_hour=reduce(operator.add, per_hour1)


im1 = Image.open("Chilton.png")
with open('area_.csv','rt',encoding='ANSI') as csvfile:
    map = csv.reader(csvfile)
    new_x = [row[0] for row in map]

    #x1 = [row[0] for row in map]
    #x1 = str(x1)
    #x2 = x1.replace("'","")

with open('area_.csv', 'r', encoding='ANSI') as csvfile:
    map = csv.reader(csvfile)
    new_y = [row[1] for row in map]

with open('area_.csv', 'r', encoding='ANSI') as csvfile:
    map = csv.reader(csvfile)
    new_level = [row[2] for row in map] #power level

d=0
while d<8760:#365
    i=0
    while i<1473:#1473
        x1 = new_x[i]
        x1_1 = eval(x1)
        x1_2 = int(x1_1)
        y1 = new_y[i]
        y1_1 = eval(y1)
        y1_2 = int(y1_1)

        level = new_level[i]

        # changing of year


        if level == 'A':
            color = (255, round(100*((per_hour[d]-min(per_hour))/(max(per_hour)-min(per_hour)))),0)
        elif level == 'B':
            color = (255, round(100+100*((per_hour[d]-min(per_hour))/(max(per_hour)-min(per_hour)))),0)
        elif level == 'C':
            if per_hour[d] > np.median(per_hour):
                color = (255, round(155 + 100 * ((per_hour[d] - np.median(per_hour)) / (max(per_hour) - np.median(per_hour)))), 0)
            elif per_hour[d] < np.median(per_hour):
                color = (round(55 * ((np.median(per_hour) - per_hour[d]) / (np.median(per_hour) - min(per_hour)))), 255, 0)
        elif level == 'D':
            color = (round(55+100*((per_hour[d]-min(per_hour))/(max(per_hour)-min(per_hour)))), 255,0)
        elif level == 'E':
            color = (round(155+100*((per_hour[d]-min(per_hour))/(max(per_hour)-min(per_hour)))), 255,0)




        draw =ImageDraw.Draw(im1)
        draw.polygon((x1_2, y1_2+8,x1_2-8, y1_2,x1_2, y1_2-8,x1_2+8, y1_2), fill=color)
        #draw.polygon((x1_2,y1_2,x2_2,y2_2,x3_2,y3_2,x4_2,y4_2),fill=color)
        i=i+1
    #im1.show()
    im2=im1.convert('RGB')
    im2.save('pic/'+str(d)+'chilton.jpg')
    d=d+1
    print(d)

# path = 'pic'
# pic = os.listdir(path)
# for name in pic:
#     index_num = pic.index(name)
#     os.renames(os.path.join(path,name),os.path.join(path,str(index_num+1)+name))

img = cv.imread('pic/0chilton.jpg')
fps = 25
# imgInfo = img.shape
# print(imgInfo[1],imgInfo[0])
size = (1040,1850)
fourcc = cv.VideoWriter_fourcc(*'mp4v')

videoWrite=cv.VideoWriter('chilton.mp4',fourcc,fps,size)

files = os.listdir('./pic')
path='pic'
out_num=len(files)
for i in range(0,out_num):
    fileName = os.getcwd() + '/pic/' + str(i) + 'chilton.jpg'
    img = cv.imread(fileName)

    videoWrite.write(img)

videoWrite.release()



