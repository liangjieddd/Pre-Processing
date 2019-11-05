from PIL import Image
import os.path
import glob


def convertjpg(jpgfile, outdir, width=100, height=200):
    img = Image.open(jpgfile)
    img_size = img.size
    width = int(img_size[0]*4)
    height = int(img_size[1]*4)

    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        imgname = os.path.basename(jpgfile)
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    except Exception as e:
        print(e)


for jpgfile in glob.glob(r"C:\Users\Administrator\Desktop\all_samples_neg\*.jpg"):
    convertjpg(jpgfile, r"C:\Users\Administrator\Desktop\all_samples_neg_mul2")
