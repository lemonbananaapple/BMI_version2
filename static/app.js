// app.js
function calculateBMI() {
    const weight = parseFloat(document.getElementById("weight").value);
    const height = parseFloat(document.getElementById("height").value);

    if (weight > 0 && height > 0) {
        const bmi = weight / (height * height);
        const bmiRounded = bmi.toFixed(2);

        let bmiCategory = "";
        if (bmi < 18.5) {
            bmiCategory = "Underweight";
        } else if (bmi < 25) {
            bmiCategory = "Normal";
        } else if (bmi < 30) {
            bmiCategory = "Overweight";
        } else {
            bmiCategory = "Obese";
        }

        document.getElementById("result").innerHTML = `Your BMI: ${bmiRounded} (${bmiCategory})`;
    } else {
        document.getElementById("result").innerHTML = "Please enter valid weight and height.";
    }
}
