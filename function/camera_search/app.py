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

# @app.route('/addCams',methods=['POST'])
# def addCams():
#     dao = CameraDAO()
#     dto = CameraDTO(request.form.get('brand'),request.form.get('model'),request.form.get('price'),request.form.get('format'))
#     dao.addCams(dto)
#     return dao.allCams(request.form.get('brand'))

# @app.route('/delCams',methods=['POST'])
# def delCams():
#     dao = CameraDAO()
#     dto = CameraDTO(request.form.get('brand'),request.form.get('model'),0,0)
#     dao.delCams(dto)
#     return dao.allCams(request.form.get('brand'))

@app.route('/showall',methods=['GET'])
def showall():
    dao = CameraDAO()
    return dao.showall()



if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")
