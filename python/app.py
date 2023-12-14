from flask import Flask
from flask import request

import json

app = Flask(__name__)

@app.route('/get', methods= ['GET'])
def get_exam():
    name = request.args.get('name')
    age = request.args.get('age')
    
    return name + "-" + age

@app.route('/post', methods=['POST'])
def post_example():
    data = json.loads(request.data)  # serialized 된 자료를 다시 dictionary로 불러옴
    name = data['name']
    age = data['age']
    
    return name + "-" + age

if __name__ == "__main__":
    app.run(debug = True, port = 8080)