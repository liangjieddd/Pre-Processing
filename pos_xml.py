import xmltodict
import os
import sys
import json
import io
import cv2
import os
from xml.dom.minidom import Document

global null
null = ''


def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                L.append(os.path.join(root, file))
        return L


path = r'C:\Users\Administrator\Desktop\round2\al_defect\POS'
label = 'POS'
m_folder = path.split(r"\\")[-1]
print('m_folder=', m_folder)
m_database = 'al_defect'
print('m_database=', m_database)
# m_depth = 3
# print('m_depth=', m_depth)
m_segmented = 0
print('m_segmented=', m_segmented)

m_pose = 'Unspecified'
print('m_pose=', m_pose)
m_truncated = 0
print('m_truncated=', m_truncated)
m_difficult = 0
print('m_difficult=', m_difficult)
m_segmented = 0
print('m_segmented=', m_segmented)

path_list = file_name(path)
for name in enumerate(path_list):
    m_path = name[1]
    dir = os.path.dirname(m_path)
    print('dir=', dir)

    # file_json = io.open(m_path, 'r', encoding='utf-8')
    # json_data = file_json.read()
    # data = json.loads(json_data)
    m_filename = m_path.split("\\")[-1].split(".")[0]+".jpg"
    print('m_filename=', m_filename)

    m_path = dir + '\\' + m_filename
    print('m_path=', m_path)

    img_path = m_path.split(".")[0]+".jpg"
    img = cv2.imread(img_path)
    img_shape = img.shape
    m_width = img_shape[1]
    print('m_width=', m_width)
    m_height = img_shape[0]
    print('m_height=', m_height)
    m_depth = img_shape[2]
    print('M_depth=',m_depth)

    object_name = os.path.splitext(m_filename)[0]
    new_object_name = object_name + '.xml'
    print(new_object_name)

    doc = Document()  # 创建DOM文档对象
    DOCUMENT = doc.createElement('annotation')  # 创建根元素

    floder = doc.createElement('floder')
    floder_text = doc.createTextNode(m_folder.split("\\")[-1])
    floder.appendChild(floder_text)
    DOCUMENT.appendChild(floder)
    doc.appendChild(DOCUMENT)

    filename = doc.createElement('filename')
    filename_text = doc.createTextNode(m_filename)
    filename.appendChild(filename_text)
    DOCUMENT.appendChild(filename)
    doc.appendChild(DOCUMENT)

    # path = doc.createElement('path')
    # path_text = doc.createTextNode(m_path)
    # path.appendChild(path_text)
    # DOCUMENT.appendChild(path)
    # doc.appendChild(DOCUMENT)

    source = doc.createElement('source')
    database = doc.createElement('database')
    database_text = doc.createTextNode(m_database)  # 元素内容写入
    database.appendChild(database_text)
    source.appendChild(database)
    DOCUMENT.appendChild(source)
    doc.appendChild(DOCUMENT)

    size = doc.createElement('size')
    width = doc.createElement('width')
    width_text = doc.createTextNode(str(m_width))  # 元素内容写入
    width.appendChild(width_text)
    size.appendChild(width)

    height = doc.createElement('height')
    height_text = doc.createTextNode(str(m_height))
    height.appendChild(height_text)
    size.appendChild(height)

    depth = doc.createElement('depth')
    depth_text = doc.createTextNode(str(m_depth))
    depth.appendChild(depth_text)
    size.appendChild(depth)

    DOCUMENT.appendChild(size)

    segmented = doc.createElement('segmented')
    segmented_text = doc.createTextNode(str(m_segmented))
    segmented.appendChild(segmented_text)
    DOCUMENT.appendChild(segmented)
    doc.appendChild(DOCUMENT)



    object = doc.createElement('object')
    name = doc.createElement('name')
    name_text = doc.createTextNode('POS')
    name.appendChild(name_text)
    object.appendChild(name)

    pose = doc.createElement('pose')
    pose_text = doc.createTextNode(m_pose)
    pose.appendChild(pose_text)
    object.appendChild(pose)

    truncated = doc.createElement('truncated')
    truncated_text = doc.createTextNode(str(m_truncated))
    truncated.appendChild(truncated_text)
    object.appendChild(truncated)

    difficult = doc.createElement('difficult')
    difficult_text = doc.createTextNode(str(m_difficult))
    difficult.appendChild(difficult_text)
    object.appendChild(difficult)

    bndbox = doc.createElement('bndbox')
    bndbox_text = doc.createTextNode('NULL')
    difficult.appendChild(difficult_text)
    object.appendChild(difficult)

    DOCUMENT.appendChild(object)

    new_path_filename = path + '/' + new_object_name
    print('new_path_filename=', new_path_filename)
    f = open(new_path_filename, 'w')

    doc.writexml(f, indent='\t', newl='\n', addindent='\t',encoding='utf-8')
    f.close()
