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
PreImNum = 2776
fileIdLen = 10
ImExpName = '.jpg'
AnotExpName = '.xml'
ImIdSet = range(1, PreImNum + 1)

# data file

ImFolder = r"C:\Users\Administrator\Desktop\al_defect_VOC\VOCdevkit\VOC2007\JPEGImages"
AnotFolder = r"C:\Users\Administrator\Desktop\al_defect_VOC\VOCdevkit\VOC2007\Annotations"
savepath = r"C:\Users\Administrator\Desktop\al_defect_GT"


##get object annotation bndbox loc start
def GetAnnotBoxLoc(AnotPath, BDD, CH, JP, JWLD, LD, PL, QK, QP, ZD, ZS):
    # open xml
    tree = ET.ElementTree(file=AnotPath)
    root = tree.getroot()
    ObjectSet = root.findall('object')
    ObjBndBoxSet = {}
    for Object in ObjectSet:
        ObjName = Object.find('name').text
        if ObjName == "BDD":
            BDD += 1
        if ObjName == "CH":
            CH += 1
        if ObjName == "JP":
            JP += 1
        if ObjName == "JWLD":
            JWLD += 1
        if ObjName == "LD":
            LD += 1
        if ObjName == "PL":
            PL += 1
        if ObjName == "QK":
            QK += 1
        if ObjName == "QP":
            QP += 1
        if ObjName == "ZD":
            ZD += 1
        if ObjName == "ZS":
            ZS += 1

        # BndBox = Object.find('bndbox')
        # x1 = int(BndBox.find('xmin').text) - 1
        # y1 = int(BndBox.find('ymin').text) - 1
        # x2 = int(BndBox.find('xmax').text) - 1
        # y2 = int(BndBox.find('ymax').text) - 1
        # BndBoxLoc = [x1, y1, x2, y2]
        # if ObjName in ObjBndBoxSet:
        # #if ObjBndBoxSet.has_key(ObjName):
        #     ObjBndBoxSet[ObjName].append(BndBoxLoc)
        # else:
        #     ObjBndBoxSet[ObjName] = [BndBoxLoc]  # why not ues dict(key=val)?
    # return ObjBndBoxSet


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
    BDD = 0
    CH = 0
    JP = 0
    JWLD = 0
    LD = 0
    PL = 0
    QK = 0
    QP = 0
    ZD = 0
    ZS = 0

    for anno in os.listdir(AnotFolder):
        # ImPreName = os.path.splitext(filename)[0]
        # # ImIdStr = str(ImId).zfill(fileIdLen)
        # ImName = ImPreName + ImExpName
        # ImPath = os.path.join(ImFolder, ImName)
        # Im = cv2.imread(ImPath, 1)
        # print ImName
        # AnotName = ImPreName + AnotExpName

        AnotPath = os.path.join(AnotFolder, anno)
        ObjBndBoxSet = GetAnnotBoxLoc(AnotPath, BDD, CH, JP, JWLD, LD, PL, QK, QP, ZD, ZS)

    print("BDD:" + str(BDD))
    print("CH:" + str(CH))
    print("JP:" + str(JP))
    print("JWLD:" + str(JWLD))
    print("LD:" + str(LD))
    print("PL:" + str(PL))
    print("QK:" + str(QK))
    print("QP:" + str(QP))
    print("ZD:" + str(ZD))
    print("ZS:" + str(ZS))

    # print(AnotName)
    # print(str(ObjBndBoxSet))
    # DrawObjectBox(Im, ObjBndBoxSet, (255, 0, 0))
    # #cv2.imshow('OriginIm', Im)
    # cv2.imwrite("/data/dlj/code/HOG_SVM_DD_FINAL/NEUData/test_images/img_rect/{}".format(str(filename)), Im)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
