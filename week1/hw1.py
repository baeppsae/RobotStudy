import cv2 as cv
import numpy as np

def mouse_callback(event, x, y, flags, param):
    if event == 1:
        print('B: ', param[y][x][0], '\nG: ', param[y][x][1], '\nR: ', param[y][x][2])
        print('=================================')


Path = 'Data/'
Name = 'rabong.jpg'
FullName = Path + Name

# 이미지 읽기
img = cv.imread(FullName)

# 여기에 소스코드 작성
sa = [4]


imgB = img[:, :, 0]
imgG = img[:, :, 1]
imgR = img[:, :, 2]

for y in range(imgB.shape[0]):
    for x in range(imgB.shape[1]):
        if imgB[x][y] < 40:
            imgB[x][y] = 0

for y in range(imgG.shape[0]):
    for x in range(imgG.shape[1]):
        if imgG[x][y] > 80:
            imgG[x][y] = 0

for y in range(imgR.shape[0]):
    for x in range(imgR.shape[1]):
        if imgR[x][y] > 150:
            imgR[x][y] = 255
            if x > 256 and y < 256:
                sa[0] += 1
            if x < 256 and y < 256:
                sa[1] += 1
            if x < 256 and y > 256:
                sa[2] += 1
            if x > 256 and y > 256:
                sa[3] += 1
max = 0
for i in 3:
    if sa[i] > sa[i+1]:
        max = sa[i]
    else max = sa[i+1]

cv.line(img, (512, 256), (0, 256), (255, 0, 0))
cv.line(img, (256, 512), (256, 0), (255, 0, 0))


cv.imshow('result', img)
# 이미지 출력
#cv.imshow('gray1', gray1)
#cv.imshow('gray', gray)
#cv.imshow('blur', blur)


cv.waitKey(0)
