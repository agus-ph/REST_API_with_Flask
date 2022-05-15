from crypt import methods
from distutils.log import debug
from flask import Flask, jsonify
from products import products

app = Flask(__name__)

@app.route("/ping")
def ping_pong():
    return jsonify({"message":"Pong!"})

if __name__ == "__main__":
    app.run(debug=False)