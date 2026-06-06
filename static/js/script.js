/*let toggle = document.getElementById ('toggle');
let label_toggle = document.getElementById ('label_toggle');

toggle.addEventListener ('change', (event) => {
    
    let checked = event.target.checked;
    document.body.classList.toggle ('dark');


    if (checked == true) {
        label_toggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
        label_toggle.style.color = 'yellow';
    } else {
        label_toggle.innerHTML = '<i class="fa-solid fa-moon"></i>';
        label_toggle.style.color = '#000';
    }
})*/

/*const eye = document.querySelector ('.input-eye');
const password = document.querySelector ('input[name="password1"]');

eye.addEventListener ('click', () => {
    if (password.type === 'password') {
        password.type = 'text';
        eye.classList.remove ('bi-eye-slash');
        eye.classList.add('bi-eye');
    } else {
        password.type = 'password';
        eye.classList.remove('bi-eye');
        eye.classList.add ('bi-eye-slash');   
    }
})*/

/*let eye = document.querySelector('.input-eye');
let password = document.querySelector('.box');

eye.addEventListener('click', () => {
    if (password.type === 'password') {
        password.type = 'text';

        eye.classList.remove('bi-eye-slash');
        eye.classList.add('bi-eye');
    } else {
        password.type = 'password';

        eye.classList.remove('bi-eye');
        eye.classList.add('bi-eye-slash');
    }
});*/

const eyes = document.querySelectorAll('.input-eye');

eyes.forEach((eye) => {
    eye.addEventListener('click', () => {
        const inputBox = eye.parentElement;
        const password = inputBox.querySelector('.box');

        if (password.type === 'password') {
            password.type = 'text';
            eye.classList.remove('bi-eye-slash');
            eye.classList.add('bi-eye');
        } else {
            password.type = 'password';
            eye.classList.remove('bi-eye');
            eye.classList.add('bi-eye-slash');
        }
    });
});