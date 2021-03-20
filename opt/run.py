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
which = []
while i < 5:
    testpic = path[i]
    it = Categorize.do_pic(testpic)
    which.append(it)
    print ('\n\n' +str(it) + '\n\n')
    
    shutil.copy(testpic, "./images/" + str(it))
    
    i += 1

print (which)

