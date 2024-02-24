# app.py
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')


@app.route("/", methods=["GET", "POST"])
def calculate_bmi():
    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])
        except ValueError:
            return "Please provide valid weight and height."

        if weight > 0 and height > 0:
            bmi = weight / (height * height)
            bmi_category = get_bmi_category(bmi)
            return f"Your BMI: {bmi:.2f} ({bmi_category})"
        else:
            return "Please enter valid weight and height."

    return render_template("bmi_form.html")

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    app.run(debug=True)
