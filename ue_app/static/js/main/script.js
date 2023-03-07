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
let addNewContent = document.querySelector('.add-new-card');
function displayCard() {
    signMenu.style.display = 'block';
}

function displayAddNewCard() {
    addNewContent.style.display = 'block';
}

function cancelsignMenu() {
    signMenu.style.display = 'none';
}
function canceladdNew() {
    addNewContent.style.display = 'none';
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

// DELETE CONTENT

let deleteBtn = document.querySelectorAll(".delete-content svg");
let deleteCard = document.querySelectorAll(".delete-pop-up");
deleteBtn.forEach((dBtn)=>{
    dBtn.addEventListener('click',()=>{
        deleteCard.forEach((dCard)=>{
            if (dBtn.classList[0] == dCard.id) {
                dCard.classList.add('displayDeleteCard');
            };
        })
    })
})

let deletePromptCard = document.querySelector(".delete-pop-up");
function cancelDeletePromptCard(btn) {
    if (btn.parentElement.parentElement.style.display != 'none') {
        btn.parentElement.parentElement.classList.remove('displayDeleteCard');
    }else{
        btn.parentElement.parentElement.classList.add('displayDeleteCard');
    }
    
}

let leftAside = document.querySelector('.recommender-channels');
function displayLeftAside(){
    leftAside.style.display = 'block';
}

function removeLeftAside(){
    leftAside.style.display = 'none';
}

// REPLY COMMENT JS

const replyCommentCont = document.querySelectorAll('.reply-comment-form-container');
let replyBtn = document.querySelectorAll(".reply-button");
// function displayReplyForm() {
//     replyBtn.forEach(rBtn => {
//         replyCommentCont.forEach(element => {
//             console.log(rBtn.classList[0], element.id)
//             if (rBtn.classList[0] == element.id) {
//                 element.classList.add('display-reply-comment-container');
//             };
//         });
//     }); 
// }

replyBtn.forEach((rBtn)=>{
    rBtn.addEventListener('click',()=>{
        replyCommentCont.forEach((rCard)=>{
            console.log(rBtn.classList[0], rBtn.id)
            if (rBtn.classList[0] == rCard.id) {
                rCard.classList.add('display-reply-comment-container');
            };
        })
        document.querySelector('.comment-form-class').classList.add('comment-form-hide');
    })
})

function displayCommentContainer() {
    document.querySelector('.comment-container').style.display = 'block';
}
function hideCommentContainer() {
    document.querySelector('.comment-container').style.display = 'none';
}