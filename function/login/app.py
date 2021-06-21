from flask import Flask, request, render_template, jsonify, redirect
from flask.helpers import url_for
from flask_jwt_extended import *
import datetime
from dto import User
from dao import Camera

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    JWT_SECRET_KEY="I'M IML"
)

jwt = JWTManager(app)


@app.route('/', methods=['get'])
def index():
    print('login Page')
    return render_template('test.html')


@app.route('/login', methods=['POST'])
def login_proc():
    user_id = request.form.get("id")
    user_pw = request.form.get("pw")
    user_info = User(user_id, user_pw)
    camera = Camera()
    check_user = camera.login(user_info)
    if check_user:
        if (user_pw == check_user[2]):
            return jsonify(result=200, access_token=create_access_token(identity=user_id))
        else:
            return jsonify(result=401)
    else:
        return jsonify(result=401)


@app.route("/login", methods=['get'])
@jwt_required()
def jwt_confirm():
    print('--------------------------------')
    cur_user = get_jwt_identity()
    # print(cur_user)
    if cur_user:
        return jsonify('login.html')
    else:
        return jsonify(result=401)


@app.route('/loginurl', methods=['get'])
def index2():
    print('login Page')
    return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True, port="5000", host="127.0.0.1")
