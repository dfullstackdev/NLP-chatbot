from flask import Flask, jsonify, request
from flask_cors import CORS
import zeroTrainer
import oneTrainer
import twoTrainer
import threeTrainer
import fourTrainer
app = Flask(__name__)
CORS(app)

@app.route('/api/zero',methods=['POST'])
def index():
    user_input = request.json['user_input']
    return jsonify({'msg':str(zeroTrainer.brain(user_input))})

@app.route('/api/one',methods=['POST'])
def index2():
    u_input = request.json['u_input']
    return jsonify({'msg':str(oneTrainer.brain(u_input))})

@app.route('/api/two',methods=['POST'])
def index3():
    Uinput = request.json['Uinput']
    return jsonify({'msg':str(twoTrainer.brain(Uinput))})

@app.route('/api/three',methods=['POST'])
def index4():
    usr_input = request.json['usr_input']
    return jsonify({'msg':str(threeTrainer.brain(usr_input))})

@app.route('/api/four',methods=['POST'])
def index5():
    input = request.json['input']
    return jsonify({'msg':str(fourTrainer.brain(input))})

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)