#!/usr/bin/python
#coding:utf-8

from datetime import datetime
import downloadimage.downloadimage

yonkoma_url = "http://www.kadokawa.co.jp/sp/soraoto/image/yonkoma/"
jpg_extension = ".jpg"

now = datetime.now()

now_string = now.strftime('%Y%m%d')

url = yonkoma_url + now_string + jpg_extension

downloadimage.downloadimage.downloadimage(url)




