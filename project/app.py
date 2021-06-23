from flask import Flask, request, render_template, jsonify, redirect
from flask_jwt_extended import *
from selftest_dto import User
from dao import Camera
from signup_dto import USERDTO
from camera_dto import CAMERADTO

app = Flask(__name__)

# 첫 화면은 카메라 추천 받는 화면으로 하자
@app.route('/', methods=['get'])
def index():
    print('recommendation Page')
    return render_template('index.html')

# 카메라 추천하는 기능
@app.route('/camfind', methods=["POST"])
def selectcam():
    dao = Camera()
    return dao.recommend(request.form.get("id"), request.form.get("pw"))

# 유저인지 확인하는 역할
@app.route('/login', methods=['POST'])
def login_proc():
    user_info = User(request.form.get("id"), request.form.get("pw"), request.form.get("test_level"))
    camera = Camera()
    camera.update_level(user_info)
    return jsonify(result=200)


# 회원가입 기능
@app.route("/signup", methods=["POST"])
def insertuser():
    dao = Camera()
    dto = USERDTO(request.form.get("u_id"), request.form.get("u_pw"), request.form.get("nick"))
    dao.userinsert(dto)
    return jsonify(result=200)

# 아이디 중복 확인
@app.route('/checkid', methods = ["POST"])
def selectid():
    dao = Camera()
    check = dao.id_check(request.form.get("u_id"))
    if check is None:
        return jsonify(True)
    else:
        return jsonify(False)

# 닉네임 중복 확인
@app.route('/checknick', methods = ["POST"])
def selectnick():
    dao = Camera()
    check = dao.nick_check(request.form.get("nick"))
    if check is None:
        return jsonify(True)
    else:
        return jsonify(False)

# 자가진단 화면으로 이동
@app.route('/selftest', methods=['get'])
def linktoselftest():
    print('link to self test Page')
    return render_template('selftest.html')
    
# 회원가입 화면으로 이동
@app.route('/signup', methods=['get'])
def linktosignup():
    print('sing up Page')
    return render_template('signup.html')

# 카메라 검색 화면으로 이동
@app.route('/search', methods=['get'])
def linktosearch():
    print('link to search search Page')
    return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True, port="5000", host="127.0.0.1")
