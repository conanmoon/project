from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

# import requests
# from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('word_analyzer.html')

@app.route('/words', methods=['GET'])
def listing():
    
    return jsonify({'result':'success'})

## API 역할을 하는 부분
@app.route('/words', methods=['POST'])
def saving():
    read_text = request.form['write_text']
    return jsonify({'result': 'success', 'texts': read_text})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)