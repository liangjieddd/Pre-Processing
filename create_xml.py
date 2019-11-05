
from xml.dom.minidom import Document




doc = Document()  # 创建DOM文档对象
DOCUMENT = doc.createElement('annotation')  # 创建根元素

floder  = doc.createElement('floder')          ##建立自己的开头
floder_text  = doc.createTextNode('JPEGImages')##建立自己的文本信息
floder.appendChild(floder_text)                ##自己的内容
DOCUMENT.appendChild(floder)
doc.appendChild(DOCUMENT)


filename  = doc.createElement('filename')
filename_text  = doc.createTextNode('00000.jpg')
filename.appendChild(filename_text)
DOCUMENT.appendChild(filename)
doc.appendChild(DOCUMENT)

path  = doc.createElement('path')
path_text  = doc.createTextNode('/home/ubuntu/JPEGImages/000000.jpg')
path.appendChild(path_text)
DOCUMENT.appendChild(path)
doc.appendChild(DOCUMENT)


source  = doc.createElement('source')
database = doc.createElement('database')
database_text = doc.createTextNode('Unknow')  # 元素内容写入
database.appendChild(database_text)
source.appendChild(database)
DOCUMENT.appendChild(source)
doc.appendChild(DOCUMENT)

size  = doc.createElement('size')
width = doc.createElement('width')
width_text = doc.createTextNode('1920')  # 元素内容写入
width.appendChild(width_text)
size.appendChild(width)

height = doc.createElement('height')
height_text = doc.createTextNode('1080')
height.appendChild(height_text)
size.appendChild(height)

depth = doc.createElement('depth')
depth_text = doc.createTextNode('3')
depth.appendChild(depth_text)
size.appendChild(depth)

DOCUMENT.appendChild(size)

segmented  = doc.createElement('segmented')
segmented_text  = doc.createTextNode('0')
segmented.appendChild(segmented_text)
DOCUMENT.appendChild(segmented)
doc.appendChild(DOCUMENT)


object  = doc.createElement('object')
name = doc.createElement('name')
name_text = doc.createTextNode('nothing')
name.appendChild(name_text)
object.appendChild(name)

pose = doc.createElement('pose')
pose_text = doc.createTextNode('Unspecified')
pose.appendChild(pose_text)
object.appendChild(pose)

truncated = doc.createElement('truncated')
truncated_text = doc.createTextNode('0')
truncated.appendChild(truncated_text)
object.appendChild(truncated)


bndbox  = doc.createElement('bndbox')
xmin = doc.createElement('xmin')
xmin_text = doc.createTextNode('342')
xmin.appendChild(xmin_text)
bndbox.appendChild(xmin)

ymin = doc.createElement('ymin')
ymin_text = doc.createTextNode('330')
ymin.appendChild(ymin_text)
bndbox.appendChild(ymin)

xmax = doc.createElement('xmax')
xmax_text = doc.createTextNode('581')
xmax.appendChild(xmax_text)
bndbox.appendChild(xmax)

ymax = doc.createElement('ymax')
ymax_text = doc.createTextNode('753')
ymax.appendChild(ymax_text)
bndbox.appendChild(ymax)
object.appendChild(bndbox)

DOCUMENT.appendChild(object)



object  = doc.createElement('object')
name = doc.createElement('name')
name_text = doc.createTextNode('nothing')
name.appendChild(name_text)
object.appendChild(name)

pose = doc.createElement('pose')
pose_text = doc.createTextNode('Unspecified')
pose.appendChild(pose_text)
object.appendChild(pose)

truncated = doc.createElement('truncated')
truncated_text = doc.createTextNode('0')
truncated.appendChild(truncated_text)
object.appendChild(truncated)



bndbox  = doc.createElement('bndbox')
xmin = doc.createElement('xmin')
xmin_text = doc.createTextNode('342')
xmin.appendChild(xmin_text)
bndbox.appendChild(xmin)

ymin = doc.createElement('ymin')
ymin_text = doc.createTextNode('330')
ymin.appendChild(ymin_text)
bndbox.appendChild(ymin)

xmax = doc.createElement('xmax')
xmax_text = doc.createTextNode('581')
xmax.appendChild(xmax_text)
bndbox.appendChild(xmax)

ymax = doc.createElement('ymax')
ymax_text = doc.createTextNode('753')
ymax.appendChild(ymax_text)
bndbox.appendChild(ymax)
object.appendChild(bndbox)

DOCUMENT.appendChild(object)
############item:Python处理XML之Minidom################

########### 将DOM对象doc写入文件
f = open('aha.xml' ,'w')

doc.writexml(f ,indent = '\t' ,newl = '\n', addindent = '\t' ,encoding='utf-8')
f.close()
