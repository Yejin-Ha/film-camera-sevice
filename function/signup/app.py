from flask import Flask, json, render_template, request, jsonify
from dao import USERDAO
from dto import USERDTO


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('reqres.html')



@app.route("/signup", methods=["POST"])
def insertuser():
    dao = USERDAO()
    dto = USERDTO(request.form.get("u_id"), request.form.get("u_pw"), request.form.get("nick"))
    dao.userinsert(dto)

    return jsonify(result=200)

@app.route('/checkid', methods = ["POST"])
def selectid():
    dao = USERDAO()
    # dto = USERDTO(request.form.get("u_id"))
    check = dao.id_check(request.form.get("u_id"))
    if check is None:
        print('hi')
        return jsonify(True)
    else:
        print('bye')
        return jsonify(False)

@app.route('/checknick', methods = ["POST"])
def selectnick():
    dao = USERDAO()
    check = dao.nick_check(request.form.get("nick"))
    if check is None:
        print('hi1')
        return jsonify(True)
    else:
        print('bye1')
        return jsonify(False)

    
    

if __name__=='__main__':
    app.run(debug=True, host="127.0.0.1", port="5000")
