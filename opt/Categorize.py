# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 02:32:17 2021

@author: tanak
"""


import keras
import sys, os


import numpy as np
from keras.models import load_model
from PIL import Image

imsize = (64, 64)


keras_param = "./cnn.h5"
testpic = "test"

def load_image(path):
    img = Image.open(path)
    img = img.convert('RGB')
    # 学習時に、(64, 64, 3)で学習したので、画像の縦・横は今回 変数imsizeの(64, 64)にリサイズします。
    img = img.resize(imsize)
    # 画像データをnumpy配列の形式に変更
    img = np.asarray(img)
    img = img / 255.0
    return img

def do_pic(testpic):
    model = load_model(keras_param)
    img = load_image(testpic)
    prd = model.predict(np.array([img]))
    print(prd) # 精度の表示
    prelabel = np.argmax(prd, axis=1) 
    if prelabel == 0:
        it = "comic"
    elif prelabel == 1:
        it = "other"
    return it

