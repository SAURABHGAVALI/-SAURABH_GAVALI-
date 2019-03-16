function calculateBMI(){
		var feet = document.getElementById("feet").value;
		var inches = document.getElementById("inches").value;
		var weight = document.getElementById("weight").value;

		if ((feet > 0) || (inches > 0) || (weight > 0)) {
			var feetToInches = parseInt(feet*12);
			var inchesToInt = parseInt(inches);
			var totalInches = feetToInches + inchesToInt;

			var bmi = (weight / (totalInches*totalInches)) * 703;
			var result = "<br> Your Body Mass Index (BMI) is " + bmi.toFixed(1);
			if (bmi<=18.5){
				result += "<br> It looks like you are underweight."
			}
			else if (bmi>18.5 && bmi<=24.9) {
				result += "<br> You have a normal weight."
			}
			else if (bmi>24.9 && bmi<=29.9) {
				result += "<br> You are overweight."
			}else {
				result += "<br> You are obese."
			} document.getElementById("output").innerHTML = result;
		} else {
			alert("Please enter a numeric value for your height and weight.");
		}		
	}
	
document.getElementById("calculateBMI").onclick = calculateBMI;
