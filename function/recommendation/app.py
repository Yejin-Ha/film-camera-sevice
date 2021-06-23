from flask import Flask, json, render_template, request, jsonify
from dao import LEVELDAO
from dto import LEVELDTO

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('reqres.html')


@app.route('/camfind', methods=["POST"])
def selectcam():
    dao = LEVELDAO()
    return dao.levelselect(request.form.get("test_level"))


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")
