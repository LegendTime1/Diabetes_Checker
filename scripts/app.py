from flask import Flask, render_template, request
from checker import predict_diabetes

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def make_prediction():
    if request.method == "POST":
        age = int(request.form.get("age"))
        insulin = float(request.form.get("insulin"))
        prediction = predict_diabetes(age, insulin)

        return render_template("result.html", prediction=prediction)

#if __name__ == "__main__":
#    app.run(debug=True)
