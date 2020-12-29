import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import PIL.Image as Image

from cv2 import cv2
import numpy as np
import os
import glob
import image_controller as cntrl


# this function take cv2.imread Obj, manipulate it, and return 4concat image
# with original and their RGB split
def imagePerRGB(img):
    blue, green, red = cv2.split(img)
    zeros = np.zeros(blue.shape, np.uint8)

    blueRGB = cv2.merge((blue, zeros, zeros))
    greenRGB = cv2.merge((zeros, green, zeros))
    redRGB = cv2.merge((zeros, zeros, red))

    image_gabung = cntrl.concat_tile([[img, blueRGB],
                                      [greenRGB, redRGB]])

    return image_gabung


if __name__ == "__main__":
    list_image = cntrl.listOfImageObj("./img_plyground/")

    first_image = list_image[3]

    split_image = imagePerRGB(first_image)

    cv2.imshow('title', split_image)

    cv2.waitKey(7000)
    cv2.destroyAllWindows()
