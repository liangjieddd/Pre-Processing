import cv2
import random
from PIL import Image
import os.path
import glob


def crop(imgfile, savePath):
    img = Image.open(imgfile)
    img_size = img.size
    width = img_size[1] - 129
    height = img_size[0] - 129

    # h、w为想要截取的图片大小
    h = 128
    w = 128
    imgname = os.path.basename(imgfile)
    list = imgname.split(".")
    imgname = list[0]

    count = 0

    if width > 0:
        if height > 0:

            # 随机产生x,y   此为像素内范围产生
            for i in range(4):
                y = random.randint(1, width)
                x = random.randint(1, height)
                # 随机截图
                box = (x, y, x + w, y + h)
                cropImg = img.crop(box)
                count += 1

                cropname = imgname + "_" + str(count) + ".jpg"

                cropImg.save(os.path.join(savePath, cropname))


if __name__ == "__main__":

    for jpgfile in glob.glob(r"C:\Users\Administrator\Desktop\all_samples_neg_mul2\*.jpg"):
        crop(jpgfile, r"C:\Users\Administrator\Desktop\all_samples_neg_crop")
