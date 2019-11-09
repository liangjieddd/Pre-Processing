# Pre-Processing
The scripts of the iamges pro-processing 

1.convert.py
铝制材料缺陷检测，将VOC格式的数据集转化为COCO格式

2.createVOC.py
将全部数据划分为trainval、train、test

3.create_xml.py
将图片信息写入xml文件中，生成标注信息

4.curves_iou.py
根据log信息进行iou曲线图的绘制，主要用于YOLOv3

5.curves_loss.py
根据log信息进行loss曲线图的绘制

6.demo.py
fast_rcnn的tensorflow版的demo

7.demo.sh
detectron2的demo文件运行脚本

8.extractJson.py
铝制材料缺陷检测中，处理数据文件的脚本，比赛提供了Json格式的数据标注格式，利用此脚本将其转化为VOC格式的标注文件

9.extract_log.py
绘制曲线图之前，在log中提取关键信息，然后进行画图

10.img_crop.py
在图片中随机裁取指定大小、指定个数的图片

11.img_resize.py
将原图resize到指定尺寸

12.img_resize_same_scale.py
将原图进行等比例放大或者缩小

13.img_resize_scale.py
将原图进行自定义比例放大或者缩小

14.overlap.py
将标注文件里的GT标注到原图上

15.pos_xml.py
为负样本（即无缺陷样本）图片生成标注框

16.proposal.py
在图片中提取负样本图片

17.resavemodel.py
tensorflow生成的模型进行重新保存

18.revisexml.py
修改xml文件中指定标签内的数据

19.save_model.py
tensorflow版本的保存模型的脚本

20.split_data.py
将数据划分为train、val、test（自定义比例）

21.voc_label.py
生成VOC格式的标签

22.write_all.py
将图片路径写入同一个txt文件中

23.write_img_to_lst.py
将图片的xml写入lst格式的文件

24.write_rect.py在原图上画Ground Truth，ps：此文件有问题，请用overlap.py

25.

26.
