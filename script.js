document.addEventListener("DOMContentLoaded", () => {
    // Hamburger Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
  
    hamburger.addEventListener('click', () => {
      navLinks.classList.toggle('active');
    });
  
    // Smooth Scrolling for Navigation Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener("click", function(e) {
        e.preventDefault();
        navLinks.classList.remove('active'); // Close mobile menu on link click
        document.querySelector(this.getAttribute("href")).scrollIntoView({
          behavior: "smooth"
        });
      });
    });
  
    // Contact Form Submission Simulation
    const contactForm = document.getElementById("contact-form");
    const formMessage = document.getElementById("form-message");
  
    contactForm.addEventListener("submit", function(e) {
      e.preventDefault();
      const name = document.getElementById("name").value.trim();
      const email = document.getElementById("email").value.trim();
      const message = document.getElementById("message").value.trim();
  
      if (name === "" || email === "" || message === "") {
        formMessage.textContent = "Please fill in all fields.";
        formMessage.style.color = "red";
        return;
      }
  
      formMessage.textContent = "Thank you for your message! I will get back to you soon.";
      formMessage.style.color = "#00adb5";
      contactForm.reset();
    });
  
    // Documents Section - File Input Preview
    const documentInput = document.getElementById('document-input');
    const documentsList = document.getElementById('documents-list');
  
    documentInput.addEventListener('change', (event) => {
      const files = event.target.files;
      documentsList.innerHTML = ''; // Clear previous documents
      Array.from(files).forEach(file => {
        const card = document.createElement('div');
  