#!/usr/bin/python
# coding:utf-8

from bs4 import BeautifulSoup
import urllib2
import urllib
import urlparse
import re

# urlのイメージを指定
url_source = "http://www.kadokawa.co.jp/sp/soraoto/"

# htmlファイルのsourceの取得
html = urllib2.urlopen(url_source).read()

# イテレータ設定
soup = BeautifulSoup(html)

elements = soup.findAll('img')

image_list = []

for e in elements:
  image_list.append(e['src']) # リストの要素に画像のURLを順次追加していく

for i in range(len(image_list)):
  #パスにはファイル名まで含めないとパーミッションのエラーになる
  save_path = '/Users/xxx/mainichicountdown/images/allimages/'
  urllib.urlretrieve(url_source + image_list[i], save_path + image_list[i].split('/')[-1])

  if image_list[i].rfind('_s'):
    urllib.urlretrieve(url_source + image_list[i].replace('_s', ''), save_path + image_list[i].split('/')[-1].replace('_s', ''))