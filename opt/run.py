# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 01:25:18 2021

@author: tanak
"""

import shutil
import Categorize
import glob
import os


keras_param = "./cnn.h5"

types = ["jpg", "png"]
img_paths = []
for ext in types:
    paths = os.path.join("./@btwn", "*.{}".format(ext))
    img_paths.extend(glob.glob(paths))

dir = "./images/comic"
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)


dir = "./images/other"
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)



 # path = glob.glob("./images/*.jpg")


i = 0
com_num = 1
oth_num = 1

which = []
while i < 20:
    testpic = img_paths[i]
    it = Categorize.do_pic(testpic)
    which.append(it)
    if (it == "comic"):
        shutil.move(testpic,"./images/comic/comic" + str(com_num) + ".jpg")
        com_num +=1
    else:
        shutil.move(testpic,"./images/other/other" + str(oth_num) + ".jpg")

    
    i += 1

print (which)

