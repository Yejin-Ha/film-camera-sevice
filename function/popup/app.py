from flask import Flask, request, render_template
from DAO import FilmDAO

app = Flask(__name__)

@app.route('/', methods = ['get'])
def first():
    return render_template('films.html')

@app.route('/getBrand',methods=['POST'])
def getBrand():
    dao = FilmDAO()
    return dao.allFilms()


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")
