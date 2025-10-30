// Toggle Password Visibility
function togglePassword() {
  const passwordField = document.getElementById("password");
  passwordField.type = passwordField.type === "password" ? "text" : "password";
}

// Login Validation
document.getElementById("loginForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();
  const errorMsg = document.getElementById("error-msg");

  // Simple Validation
  if (email === "" || password === "") {
    errorMsg.textContent = "Please fill in all fields.";
    return;
  }

  // Dummy Credentials for Testing
  const dummyEmail = "user@vehicletracker.com";
  const dummyPassword = "12345";

  if (email === dummyEmail && password === dummyPassword) {
    errorMsg.style.color = "green";
    errorMsg.textContent = "Login Successful! Redirecting...";
    setTimeout(() => {
      window.location.href = "dashboard.html"; // Change to your dashboard
    }, 1500);
  } else {
    errorMsg.style.color = "red";
    errorMsg.textContent = "Invalid email or password!";
  }
});