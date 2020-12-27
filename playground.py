import os
import PIL.Image as Image
import sys
import imghdr
from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

directory = "./img_plyground/"
CONVERTED_IMG_DIR = './converted_img/'


def openImageIterate():
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            image = Image.open(directory+filename)
            image.convert('RGB').save(CONVERTED_IMG_DIR+filename)
            continue
        else:
            continue


def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])


def drive_test():
    objectOfImages = []
    for index, filename in enumerate(os.listdir(directory)):
        if filename.endswith(".jpg") and index < 16:
            image = cv2.imread(directory + filename)
            image_s = cv2.resize(image, dsize=(300, 300))
            objectOfImages.append(image_s)
            index += 1
    return objectOfImages


def resizeToNIM(img, angkatan=2018, nim=344):
    if isinstance(img, np.ndarray):
        image = img
    else:
        image = cv2.imread(img)
    image_s = cv2.resize(image, dsize=(angkatan, nim))
    return image_s


def rotateImg90Degree(img):
    if isinstance(img, np.ndarray):
        image = img
    else:
        image = cv2.imread(img)
    image_90Degree = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    return image_90Degree


def rotateImg180Degree(img):
    if isinstance(img, np.ndarray):
        image = img
    else:
        image = cv2.imread(img)
    image_180Degree = cv2.rotate(image, cv2.ROTATE_180)
    return image_180Degree


def rotateImg270Degree(img):
    if isinstance(img, np.ndarray):
        image = img
    else:
        image = cv2.imread(img)
    image_270Degree = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return image_270Degree


def rotateImg360Degree(img):
    if isinstance(img, np.ndarray):
        image = img
    else:
        image = cv2.imread(img)
    return image


def isclass(obj):
    return isinstance(obj, type)


if __name__ == "__main__":

    ###########################################################################################

    list_img = drive_test()
    im1 = rotateImg90Degree(list_img[0])
    im2 = rotateImg180Degree(list_img[1])
    im3 = rotateImg270Degree(list_img[2])
    im4 = rotateImg360Degree(list_img[3])

    list2d_img = [[im1, im2],
                  [im3, im4]]

    gabungan = concat_tile(list2d_img)
    gabungan_tranpose = cv2.transpose(gabungan)

    gabung_test = [[gabungan, gabungan_tranpose]]
    test_gambar = concat_tile(gabung_test)
    test_gambarResize = resizeToNIM(test_gambar, 1000, 1000)
    # TODO SAVE IT AFTER THIS
    print(test_gambarResize.shape[0], test_gambarResize.shape[1])

    cv2.imshow("final_image", test_gambar)
    cv2.imshow("final_imageRes", test_gambarResize)
    # cv2.imshow("im1", im1)
    # cv2.imshow("im2", im2)
    # cv2.imshow("im3", im3)
    # cv2.imshow("im4", im4)
    # cv2.imshow("gabungan", gabungan)
    # cv2.imshow("gabungan_transpose", gabungan_tranpose)
    print(isinstance(gabungan, np.ndarray))
    print(test_gambar/255)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()

    ###########################################################################################

    # list_img = drive_test()
    # cv2.imshow("Title", list_img[15])
    # im_tile = concat_tile([list_img[:8], list_img[8:]])
    # cv2.imwrite('opencv_concat_tile.jpg', im_tile)

    # imageResize = resizeToNIM('opencv_concat_tile.jpg')
    # lebar, tinggi, channel = imageResize.shape
    # print(tinggi, lebar)
    # print(imghdr.what('opencv_concat_tile.jpg'))
    # cv2.imshow("Title", imageResize)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    ###########################################################################################
    # list_ofImage = ['apple_1.jpg', 'apple_2.jpg', 'apple_3.jpg']
    # im1 = cv2.imread(list_ofImage[0])
    # im2 = cv2.imread(list_ofImage[1])
    # im3 = cv2.imread(list_ofImage[2])

    # im1_s = cv2.resize(im1, dsize=(300, 300))
    # im2_s = cv2.resize(im2, dsize=(300, 300))
    # im3_s = cv2.resize(im3, dsize=(300, 300))

    # im_tile = concat_tile([[im1_s, im1_s, im1_s],
    #                        [im2_s, im3_s, im2_s],
    #                        [im3_s, im3_s, im3_s]])

    # cv2.imwrite('opencv_concat_tile.jpg', im_tile)

    ###########################################################################################
