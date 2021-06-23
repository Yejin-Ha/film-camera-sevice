from flask import Flask, request, render_template
from DAO import CameraDAO
from DTO import CameraDTO

app = Flask(__name__)

@app.route('/', methods = ['get'])
def first():
    return render_template('camera.html')

@app.route('/getBrand',methods=['POST'])
def getBrand():
    dao = CameraDAO()
    return dao.allCams(request.form.get('brand'),request.form.get('category'),request.form.get('test_level'))


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")
