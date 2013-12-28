#!/usr/bin/python
#coding:utf-8

import sys, urllib
import os.path
from datetime import datetime

yonkoma_url = "http://www.kadokawa.co.jp/sp/soraoto/"

now = datetime.now()

now_string = now.strftime('%Y%m%d')

url = yonkoma_url

page = urllib.urlopen(url)
localfile = open( "pages/" + now_string + ".html", 'wb')
localfile.write(page.read())
page.close()
localfile.close()
