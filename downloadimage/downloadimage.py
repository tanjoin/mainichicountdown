#!/usr/bin/python
#coding:utf-8

import sys, urllib
import os.path

def downloadimage(url):
  img = urllib.urlopen(url)
  localfile = open( "images/" + os.path.basename(url), 'wb')
  localfile.write(img.read())
  img.close()
  localfile.close()

