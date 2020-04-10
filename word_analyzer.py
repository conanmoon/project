from flask import Flask, render_template, jsonify, request
import requests
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

# import requests
# from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# URL을 읽어서 HTML를 받아오고,
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('http://0.0.0.0:5000/')
#
# # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup = BeautifulSoup(data.text, 'html.parser')
#
# # select를 이용해서, tr들을 불러오기
# texts = soup.select('#fileDisplayArea')

# movies (tr들) 의 반복문을 돌리기
# for text in texts:
#     # movie 안에 a 가 있으면,
#     a_tag = texts.select()
#     if a_tag is not None:
#         # a의 text를 찍어본다.
#         print (a_tag.text)

from selenium import webdriver

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('word_analyzer_2.html')

## API 역할을 하는 부분
@app.route('/words', methods=['POST'])
def saving():
    # read_text = request.form['write_text']
    read_text = request.form['write_text']
    print(read_text)
    # DB에 삽입할 text 만들기
    text = {
       'texts': read_text,
    }
    # texts에 text 저장하기
    # text_1 =
    db.texts.insert_one(text)
    # text_2 = db.texts.find_one({'texts': text_1})
    # texts = db.texts.update_one({'texts': text},{'$set':{'texts':text_2}})
    return jsonify({'result': 'success'})

@app.route('/words', methods=['GET'])
def listing():
    # rjson = r.json()
    read_text = request.args.get('write_text')
    print(read_text)
    texts = list(db.texts.find({},{'_id':0}))
    return jsonify({'result':'success', 'texts': texts})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

wd = webdriver.chrome()
wd.get("http://0.0.0.0:5000/")
wd.execute_script("return 5")
wd.execute_script("return true")
wd.execute_script("return {foo: 'bar'}")
wd.execute_script("return foobar()")