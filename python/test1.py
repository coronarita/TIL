from flask import Flask
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def hello():
    return "안녕 난 천재야!"

if __name__ == "__main__":
    app.run(debug = True)