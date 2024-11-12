document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');

    if (form) {
        form.addEventListener('submit', function(event) {
            let isValid = true;
            const email = form.email.value;
            const message = form.message.value;

            form.email.classList.remove('error');
            form.message.classList.remove('error');

            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                form.email.classList.add('error');
                isValid = false;
            }

            if (!message) {
                form.message.classList.add('error');
                isValid = false;
            }

            if (!isValid) {
                event.preventDefault();
                alert("Please fix the errors in the form.");
            }
        });
    }
});