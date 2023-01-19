let collapseIcon = document.querySelector('.collapse');
let sideBar = document.querySelector('.recommender-channels');
let expandIcon = document.querySelector('.expand');
let sidebarTag = document.querySelector('.collapse-title-popup-tag');
let sideBarTitle = document.querySelector('.title h3');
let displayName = document.querySelector('.account-name');
let onlineStatusViews = document.querySelector('.online-status-views');
let popularVideos = document.querySelectorAll('.recommended-videos')

function collapse() {
    sideBar.style.width = '50px';
    sideBarTitle.classList.add('remove-element');
    displayName.classList.add('remove-element');
    onlineStatusViews.classList.add('remove-element');
    expandIcon.classList.remove('remove-element');
    sidebarTag.classList.remove('remove-element');
    collapseIcon.classList.add('remove-element');
    popularVideos.forEach((ele) => ele.classList.add('remove-element'));
}
function expand(e) {
    e.preventDefault();
    sideBar.style.width = '235px';
    sideBarTitle.classList.remove('remove-element');
    displayName.classList.remove('remove-element');
    onlineStatusViews.classList.remove('remove-element');
    collapseIcon.classList.remove('remove-element');
    expandIcon.classList.add('remove-element');
    sidebarTag.classList.add('remove-element');
    popularVideos.forEach((ele) => ele.classList.remove('remove-element'));
}
collapseIcon.addEventListener('click', collapse);
expandIcon.addEventListener('click', expand);