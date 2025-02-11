from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])     #GET / POST
def hello_world():
    # Capture User data
    if request.method == "POST":
        name1 = request.form.get("name1")
        name2 = request.form.get("name2")
        name3 = request.form.get("name3")

        total = [name1, name2, name3]
        return render_template('index.html', name=total)

    # 2D Array

    # Pass to Predict Function

    # Prediction from predict function => frontend

    return render_template('index.html', name='sajeel')


if __name__ == "__main__":
    app.run(debug=True)