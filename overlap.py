# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/07/11 by DQ

import cv2
import os

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

ImSize = [200, 200]
PreImNum = 1800
fileIdLen = 6
ImExpName = '.jpg'
AnotExpName = '.xml'
ImIdSet = range(1, PreImNum + 1)

# data file
MainFolder = r'D:\deeplearning_workspace\write_rect_on_image\NEU-DET'
ImFolder = "/home/dlj/CornerNet/val_orig_result"
AnotFolder = "/home/dlj/CornerNet/data/coco/images/minival2014/Annotations"
savePath = "/home/dlj/CornerNet/visual_img/"


##get object annotation bndbox loc start
def GetAnnotBoxLoc(AnotPath):
    # open xml
    tree = ET.ElementTree(file=AnotPath)
    root = tree.getroot()
    ObjectSet = root.findall('object')
    ObjBndBoxSet = {}
    for Object in ObjectSet:
        ObjName = Object.find('name').text
        BndBox = Object.find('bndbox')
        x1 = int(BndBox.find('xmin').text) - 1
        y1 = int(BndBox.find('ymin').text) - 1
        x2 = int(BndBox.find('xmax').text) - 1
        y2 = int(BndBox.find('ymax').text) - 1
        BndBoxLoc = [x1, y1, x2, y2]
        if ObjName in ObjBndBoxSet:
            # if ObjBndBoxSet.has_key(ObjName):
            ObjBndBoxSet[ObjName].append(BndBoxLoc)
        else:
            ObjBndBoxSet[ObjName] = [BndBoxLoc]  # why not ues dict(key=val)?
    return ObjBndBoxSet


##get object annotation bndbox loc end

##draw all bndbox on image
def DrawObjectBox(Im, ObjBndBoxSet, BoxColor):
    for ObjName, BndBoxSet in ObjBndBoxSet.items():
        for BndBox in BndBoxSet:
            cv2.rectangle(Im, (BndBox[0], BndBox[1]), (BndBox[2], BndBox[3]), BoxColor, 2)
            dsptxt = '{:s}'.format(ObjName)
            cv2.putText(Im, dsptxt, (max([(BndBox[0] + BndBox[2]) // 2 - 10, 0]), max([BndBox[3] - 3, 0])),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)


if __name__ == "__main__":
    # for ImId in ImIdSet:
    for filename in os.listdir(ImFolder):
        ImPreName = os.path.splitext(filename)[0]
        # ImIdStr = str(ImId).zfill(fileIdLen)
        ImName = ImPreName + ImExpName
        ImPath = os.path.join(ImFolder, ImName)
        Im = cv2.imread(ImPath, 1)
        # print ImName
        AnotName = ImPreName + AnotExpName
        AnotPath = os.path.join(AnotFolder, AnotName)
        ObjBndBoxSet = GetAnnotBoxLoc(AnotPath)
        print(AnotName)
        print(str(ObjBndBoxSet))
        DrawObjectBox(Im, ObjBndBoxSet, (0, 255, 0))
        # cv2.imshow('Img_Res', Im)
        savePath = os.path.join("/home/dlj/CornerNet/visual_img/",filename)
        cv2.imwrite(savePath, Im)

        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
