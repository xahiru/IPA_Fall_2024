document.getElementById('contactForm').addEventListener('submit', function(event) {
    let error = '';
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    if (name.trim() === '') {
        error += 'Name is required. ';
    }
    if (email.trim() === '') {
        error += 'Email is required. ';
    }
    if (message.trim() === '') {
        error += 'Message is required.';
    }

    if (error) {
        event.preventDefault();
        document.getElementById('error').textContent = error;
    }
});