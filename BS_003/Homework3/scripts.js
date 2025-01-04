document.addEventListener("DOMContentLoaded", function () {
  const now = new Date();
  const hours = now.getHours();
  let greeting;

  if (hours < 12) {
    greeting = "Good Morning!";
  } else if (hours < 18) {
    greeting = "Good Afternoon!";
  } else {
    greeting = "Good Evening!";
  }

  document.getElementById("welcome-message").textContent = greeting;

  const contactForm = document.getElementById("contactForm");
  contactForm.addEventListener("submit", function (event) {
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert("Please enter a valid email address.");
      event.preventDefault();
      return;
    }

    if (message.trim() === "") {
      alert("Message field cannot be empty.");
      event.preventDefault();
      return;
    }
  });

  const darkModeToggle = document.getElementById("darkModeToggle");
  if (localStorage.getItem("dark-mode") === "true") {
    document.body.classList.add("dark-mode");
  }

  darkModeToggle.addEventListener("click", function () {
    document.body.classList.toggle("dark-mode");
    localStorage.setItem("dark-mode", document.body.classList.contains("dark-mode"));
  });

  const menuToggle = document.querySelector(".menu-toggle");
  const navMenu = document.querySelector("nav ul");

  menuToggle.addEventListener("click", function () {
    navMenu.classList.toggle("open");
  });
});
