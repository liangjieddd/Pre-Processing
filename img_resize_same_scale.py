import cv2
import os
from PIL import Image

def resize_scale(img, savePath):
    img = cv2.imread(img)
    imgInfo = img.shape
    print(imgInfo)
    height = imgInfo[0]
    width = imgInfo[1]
    mode = imgInfo[2]

    dstHeight = int(height * 2)
    dstWidth = int(width * 2)
    dst = cv2.resize(img, (dstWidth, dstHeight))
    dst.save(os.path.join(savePath,os.path.basename(img)))

if __name__ == "__main__":
    imgPath = r"C:\Users\Administrator\Desktop\patches"
    savePath = r"C:\Users\Administrator\Desktop\patches_mul2\\"

    for image in os.listdir(imgPath):
        img = os.path.join(imgPath,image)
        resize_scale(img,savePath)
