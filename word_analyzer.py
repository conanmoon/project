import driver as driver
from flask import Flask, render_template, jsonify, request

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

import textract

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

# #set the path to chrome driver
# # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
# # driver.get("<body>")
#
# content = driver.page_source
# soup = BeautifulSoup(content)
# for a in soup.findAll('pre', attrs={'id': 'fileDisplayArea'}):
#     texts=a.find('pre', attrs={'id':'fileDisplayArea'})
#     texts.append(texts.text)

import os
# import webapp2
# import MySQLdb
import json
import logging
import googlemaps
import jinja2
import sys
import urllib
# import urllib2
import json as simplejson
import codecs

# reload(sys)
# sys.setdefaultencoding('utf-8')
from operator import eq
from datetime import datetime
from collections import OrderedDict

# @app.route('/words', methods=['POST'])
# def post():
#
#         jsonData = json.loads(post('data'))
#
# #   penalty = self.request.get('data')
#
# #   phone = urllib.request.urlopen(req).read()
# #   data = urllib.requset.urlopen("http://www.daum.net").read()
# #   phone=urllib2.urlopen("https://firststep-2016.appspot.com/Log").read()
#
#         self.response.headers['Content-Type']='text/plain'
#         cursor = db.cursor()
#         cursor.execute("SET names utf8")
#         cursor.execute('SET SQL_SAFE_UPDATES=0;')
#         cursor.execute("""update User set text='%s' where no='%s' """%(jsonData.text))
#         db.commit()
#         db.close()

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('word_analyzer.html')


## API 역할을 하는 부분
@app.route('/words', methods=['POST'])
def write_texts():
    write_file = request.form['write_file']
    db.texts.insert_one(write_file)
    return jsonify({'result': 'success', 'write': write_file})


@app.route('/words', methods=['GET'])
def read_texts():
    read_file = db.texts.find({},{'_id':0})
    # read_text = request.form['read_text']
    return jsonify({'result': 'success', 'read': read_text})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)