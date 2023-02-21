function checkPasswordStrength(password) {
	var strength = 0;
	if (password.match(/[a-z]+/)) {
		strength += 1;
	}
	if (password.match(/[A-Z]+/)) {
		strength += 1;
	}
	if (password.match(/[0-9]+/)) {
		strength += 1;
	}
	if (password.match(/[$@#&!]+/)) {
		strength += 1;
	}
	if (password.length >= 8) {
		strength += 1;
	}
	return strength;
}

var passwordInput = document.getElementById("password");
passwordInput.addEventListener("input", function() {
	var password = passwordInput.value;
	var strength = checkPasswordStrength(password);
	var strengthText = "";
	switch (strength) {
		case 0:
			strengthText = "Too weak";
			break;
		case 1:
			strengthText = "Weak";
			break;
		case 2:
			strengthText = "Moderate";
			break;
		case 3:
			strengthText = "Strong";
			break;
		case 4:
			strengthText = "Very strong";
			break;
	}
	var strengthElement = document.getElementById("strength");
	strengthElement.innerText = strengthText;
});
