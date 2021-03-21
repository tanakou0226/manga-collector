# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 01:25:18 2021

@author: tanak
"""

import shutil
import Categorize
import glob


keras_param = "./cnn.h5"
print("アカウント名を下に入力")
val = input()


path = glob.glob("./images/*.jpg")


i = 0
com_num = 1
oth_num = 1

which = []
while i < 25:
    testpic = path[i]
    it = Categorize.do_pic(testpic)
    which.append(it)
    if (it == "comic"):
        shutil.move(testpic,"./images/comic/comic" + str(com_num) + ".jpg")
        com_num +=1
    else:
        shutil.move(testpic,"./images/other/other" + str(oth_num) + ".jpg")

    
    i += 1

print (which)

