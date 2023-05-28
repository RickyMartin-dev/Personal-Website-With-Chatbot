#from email.mime import message
from flask import Flask,render_template,request,jsonify
from src.chat import get_response

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template('index.html')

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

@app.route("/aboutme")
def aboutme():
    return render_template("aboutMe.html")
@app.route("/blog")
def blog():
    return render_template("blog.html")

if __name__ == "__main__":
    app.run(debug=True)