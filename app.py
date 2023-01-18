from email.mime import message
from flask import Flask,render_template,request,jsonify
from train_bot.chat import get_response

app = Flask(__name__)

@app.get("/")

def index_get():
    return render_template('base.html')


@app.post("/predict")
def predict():
    text = request.get_json().get("message")

    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

@app.route("/resume")
def resume():
    return render_template("resume.html")

if __name__ == "__main__":
    app.run(debug=True)