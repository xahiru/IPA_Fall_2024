// Smooth Scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Form Validation
document.getElementById("form").addEventListener("submit", function(event) {
        event.preventDefault();

        validateInputs();
    });

const setError=(element, message) => {
    const inputControl= element.parentElement;
    const errorDisplay= inputControl.querySelector('.error');

    errorDisplay.innerText= message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success');
}
const setSuccess =(element) => {
    const inputControl= element.parentElement;
    const errorDisplay= inputControl.querySelector('error');

    errorDisplay.innerText= '';
    inputControl.classList.remove('error');
    inputControl.classList.add('success');
}

const validateInputs=()=>{

    const name = document.getElementById("name");
    const number = document.getElementById("number");
    const email = document.getElementById("email");
    const message = document.getElementById("message");

    const nameValue = name.value.trim();
    const numberValue = number.value.trim();
    const emailValue = email.value.trim();
    const messageValue= message.value.trim();
}
    let isValid = true;

    if (nameValue=== '') {
        setError(name, "Please enter your name.");
    }
    else{
        setSuccess(name);
    }

    if (numberValue === '') {
        setError(number, "Please enter your number.");
    }
    else{
        setSuccess(number);
    }

    if (emailValue === '') {
        setError(email, "Please enter your email.");
    }
    else{
        setSuccess(email);
    }

    if (messageValue == '') {
        setError(message, "Please enter your message.");
    }
    else{
        setSuccess(message);
    }
    
    if(isValid){
        alert("Form submitted successfully!");
    }

// Real-Time Search Filtering
const searchInput= document.getElementById('search');
const listItems= document.querySelectorAll('#list li')

searchInput.addEventListener('input', function() {
    const searchValue = searchInput.value.toLowerCase();

    listItems.forEach(item => {
        const text = item.textContent.toLowerCase();
        item.style.display = text.includes(searchValue) ? 'block' : 'none';
    });
});