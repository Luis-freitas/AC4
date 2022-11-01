from flask import Flask, jsonify 
from model import Calculo

app = Flask(__name__)

@app.route('/calcular', methods=["GET"])
def consultar():
    return jsonify(Calculo.calcular(4, 2))

if __name__ == '__main__':
  app.run(debug=True)