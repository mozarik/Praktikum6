import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import PIL.Image as Image

from cv2 import cv2
import numpy as np
import os
import glob

files = glob.glob('/YOUR/PATH/*')
for f in files:
    os.remove(f)

# Image form https://www.kaggle.com/mbkinaci/fruit-images-for-object-detection

SIZE_GAMBAR_PX = (2018, 2 * 72 + 200)
CONVERTERD_IMG_DIR = "./converted_img/"
IMG_PLYGROUND_DIR = "./img_plyground/"
DEFAULT_IMG_DIR = "./img/train/"


# convertAllImageToJpg and save it to conv_dir
# ---
def convertAllImageToJpg(directory, conv_dir):
    for index, filename in enumerate(os.listdir(directory)):
        if filename.endswith(".jpg") and index < 16:
            image = Image.open(directory+filename)
            image.convert('RGB').save(conv_dir + filename)
            index += 1
            continue
        else:
            continue


# Empty the directory
# ---
def emptyTheDir(dir):
    files = glob.glob(dir+'*')
    for f in files:
        os.remove(f)


# Menggabungkan obj.img mengikuti pola list 2D ex [[ex1,ex1],[ex2,ex2]] akan
# mengembalikan obj.img dalam bentuk matrix tersebut
# ----
def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])


# Return a list of image object in a dir, max image is 16
def listOfImageObj(directory):
    objectOfImages = []
    for index, filename in enumerate(os.listdir(directory)):
        if filename.endswith(".jpg") and index < 16:
            image = cv2.imread(directory + filename)
            image_s = cv2.resize(image, dsize=(300, 300))
            objectOfImages.append(image_s)
            index += 1
    return objectOfImages


# Return cv2.img.obj with size of your NIM
# ----
def resizeToNIM(img):
    image = cv2.imread(img)
    image_s = cv2.resize(image, dsize=(2018, 344))
    return image_s


if __name__ == "__main__":
    convertAllImageToJpg(IMG_PLYGROUND_DIR, CONVERTERD_IMG_DIR)
    # emptyTheDir(CONVERTERD_IMG_DIR)
