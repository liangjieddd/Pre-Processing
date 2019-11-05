from PIL import Image
import os.path
import glob


def convertjpg(jpgfile, outdir, width=100, height=200):
    img = Image.open(jpgfile)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    except Exception as e:
        print(e)


for jpgfile in glob.glob(r"C:\Users\Administrator\Desktop\patches\*.jpg"):
    convertjpg(jpgfile, r"C:\Users\Administrator\Desktop\patches_100200")
