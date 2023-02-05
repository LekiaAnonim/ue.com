let shareBtn = document.querySelectorAll('.share-btn');
let shareContainer = document.querySelector('.social-share-container')

shareBtn.forEach(btn => {
    btn.addEventListener('click', () => {
        shareContainer.style.display = 'flex';
        shareContainer.style.flexWrap = 'wrap';
    })
});

let cancelShareBtn = document.querySelector('.cancel-share');
function cancelShare() {
    shareContainer.style.display = 'none';
}

// let signBtn = document.querySelector('.signup');
// let signContainer = document.querySelector('.signup-login-container');
// signBtn.addEventListener('click', () => {
//     signContainer.style.display = 'flex';
//     signContainer.classList.add('display-sign-container');
// })


let userAvatar = document.querySelector('.user-avatar');
let signMenu = document.querySelector('.user-avatar-account-card');
function displayCard() {
    signMenu.style.display = 'block';
}
function cancelsignMenu() {
    signMenu.style.display = 'none';
}
let banner  = document.querySelector('.banner')
function cancelBanner() {
    banner.style.display = 'none';
}

let messageAlert  = document.querySelector('.message-alert')
function cancelMessage() {
    messageAlert.style.display = 'none';
}



function showPassword(checkbox) {
    let passwordInput = document.querySelectorAll("input[type='password']");
    passwordInput.forEach((input) => {
        if (checkbox.checked === true) {
            input.type = "text";
        } else {
            input.type = "password";
        }
    })
  
}

let password1Input = document.querySelector("input[name='password1']");
let password2Input = document.querySelector("input[name='password2']");

setInterval(() => {
    if (password2Input.value == password1Input.value) {
        password2Input.style.color = 'green';
    } else {
        password2Input.style.color = 'red';
    }
}, 500);
