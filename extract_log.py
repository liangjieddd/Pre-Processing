import inspect
import os
import random
import sys
def extract_log(log_file, new_log_file, key_word):
    with open(log_file, 'r') as f:
      with open(new_log_file, 'w') as train_log:
  #f = open(log_file)
    #train_log = open(new_log_file, 'w')
        for line in f:
    # 去除多gpu的同步log
          if 'Syncing' in line:
            continue
    # 去除除零错误的log
          if 'nan' in line:
            continue
          if key_word in line:
            train_log.write(line)
    f.close()
    train_log.close()

extract_log('train_log_iou40000.txt','train_log_iou40000_r82.txt','Region 82')
extract_log('train_log_iou40000.txt','train_log_iou40000_r94.txt','Region 94')
