import xml.etree.ElementTree as ET
import os

def change_xml(xml_path):
    filelist = os.listdir(xml_path)
    print(filelist)
    # 打开xml文档
    for xmlfile in filelist:
        doc = ET.parse(xml_path + xmlfile)
        root = doc.getroot()
        sub1 = root.find('filename')  # 找到filename标签，
        filename = xmlfile.split(".")[0]
        # filename = filename+".xml"
        sub1.text = filename  # 修改标签内容
        doc.write(xml_path + xmlfile)  # 保存修改

if __name__ == "__main__":
    change_xml(r'C:\Users\Administrator\Desktop\NEU_COCO\VOCdevkit\VOC2007\Annotations\\')
