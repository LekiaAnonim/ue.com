let shareBtn = document.querySelectorAll('.share-btn');
let shareContainer = document.querySelector('.social-share-container')

shareBtn.forEach(btn => {
    btn.addEventListener('click', () => {
        shareContainer.style.display = 'flex';
        shareContainer.style.flexWrap = 'wrap';
    })
});

let cancelShareBtn = document.querySelector('.cancel-share');

cancelShareBtn.addEventListener('click', () => {
    shareContainer.style.display = 'none';
})