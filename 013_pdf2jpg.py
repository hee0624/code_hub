#!/usr/bin/env python
# coding=utf-8
import os
from pdf2image import convert_from_path
import shutil
import cv2
import fire

def pdf2img(pdf_path, img_dir):
    """
    :param pdf_path: pdf路径
    :param img_dir: img保存路径
    :return:
    python pdf2img.py 1.pdf sdf
    """
    pdf_path = str(pdf_path)
    img_dir = str(img_dir)
    if os.path.exists(pdf_path):
        pass
    else:
        raise ValueError(f'{pdf_path} not exists')
    if os.path.exists(img_dir):
        pass
    else:
        os.makedirs(img_dir)
    if os.path.isfile(pdf_path):
        images = convert_from_path(pdf_path=pdf_path)
        for idx, img in enumerate(images):
            img_name='{}.jpg'.format(idx)
            img_path = os.path.join(img_dir, img_name)
            img.save(img_path, 'JPEG')
    elif os.path.isdir(pdf_path):
        for rt, dirs, fiers in os.walk(pdf_path):
            for f in fiers:
                name, ext = os.path.splitext(f)
                f = os.path.join(rt, f)
                if ext in ['.jpg', '.JPG', '.png', '.PNG']:
                    shutil.copy(f, img_dir)
                elif ext in ['.pdf']:
                    os.makedirs(os.path.join(img_dir, name))
                    images = convert_from_path(pdf_path=f, thread_count=6)
                    for idx, img in enumerate(images):
                        img_name='{}.jpg'.format(idx)
                        png_path = os.path.join(os.path.join(img_dir, name), img_name)
                        img.save(png_path, 'JPEG')
    else:
        pass








if __name__ == '__main__':
    #pdf2img(pdf_path='pdf1/test_ccb_1.pdf', img_dir='jpg1')
    fire.Fire(pdf2img)


