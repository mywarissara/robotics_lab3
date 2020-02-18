
import cv2
import numpy as np

def callback(data):
    pass

while True:
    src = cv2.imread("img.png", cv2.IMREAD_COLOR)
    img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    cv2.imshow('img',src)
    cv2.imshow('binary',thresh)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()




# cv2.namedWindow('image')
# cv2.createTrackbar('h1','image',0, 255, callback)
# cv2.createTrackbar('h2','image',0, 255, callback)
# cv2.createTrackbar('s1','image',0, 255, callback)
# cv2.createTrackbar('s2','image',0, 255, callback)
# cv2.createTrackbar('v1','image',0, 255, callback)
# cv2.createTrackbar('v2','image',0, 255, callback)


# while True:
#     src = cv2.imread("img.png", cv2.IMREAD_COLOR)
#     img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # h1 = cv2.getTrackbarPos('h1','image')
    # h2 = cv2.getTrackbarPos('h2','image')
    # s1 = cv2.getTrackbarPos('s1','image')
    # s2 = cv2.getTrackbarPos('s2','image')
    # v1 = cv2.getTrackbarPos('v1','image')
    # v2 = cv2.getTrackbarPos('v2','image')

    # ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    # lower_color = np.array([h1,s1,v1])
    # upper_color = np.array([h2,s2,v2])
    # mask = cv2.inRange(img, lower_color, upper_color)
    # res = cv2.bitwise_and(src, src, mask= mask)

    # cv2.imshow('img',src)
    # cv2.imshow('binary',thresh)
    # if cv2.waitKey(1) == 27:
    #     cv2.destroyAllWindows()
