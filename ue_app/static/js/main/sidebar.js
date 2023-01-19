let collapseIcon = document.querySelector('.collapse');
let sideBar = document.querySelector('.recommender-channels');
let sideBar2 = document.querySelector('.left-sidbar');
let expandIcon = document.querySelector('.expand');
let cancelSideBarBtn = document.querySelector('.place-horizontal');
let sidebarTag = document.querySelector('.collapse-title-popup-tag');
let sideBarTitle = document.querySelector('.title h3');
let displayName = document.querySelector('.account-name');
let onlineStatusViews = document.querySelector('.online-status-views');
let popularVideos = document.querySelectorAll('.recommended-videos')

function collapse() {
    sideBar.style.width = '50px';
    sideBar.style.height = '100%';
    sideBarTitle.classList.add('remove-element');
    displayName.classList.add('remove-element');
    onlineStatusViews.classList.add('remove-element');
    expandIcon.classList.remove('remove-element');
    cancelSideBarBtn.classList.remove('remove-element');
    sidebarTag.classList.remove('remove-element');
    collapseIcon.classList.add('remove-element');
    popularVideos.forEach((ele) => ele.classList.add('remove-element'));
    sideBar.style.float = 'left';
    sideBar2.style.float = 'left';
    sideBar2.classList.remove('flex-center');
    sideBar.classList.remove('flex-center');
    expandCollapse.classList.remove('flex-center');
    sidebarHead.classList.remove('flex-center');
    reccAccts.forEach(element => {
        element.classList.remove('flex-center');
    });
}
function expand(e) {
    e.preventDefault();
    sideBar.style.width = '235px';
    sideBarTitle.classList.remove('remove-element');
    displayName.classList.remove('remove-element');
    onlineStatusViews.classList.remove('remove-element');
    collapseIcon.classList.remove('remove-element');
    expandIcon.classList.add('remove-element');
    cancelSideBarBtn.classList.add('remove-element');
    sidebarTag.classList.add('remove-element');
    popularVideos.forEach((ele) => ele.classList.remove('remove-element'));
    sideBar.style.float = 'left';
    sideBar2.style.float = 'left';
    sideBar2.classList.remove('flex-center');
    sideBar.classList.remove('flex-center');
    expandCollapse.classList.remove('flex-center');
    sidebarHead.classList.remove('flex-center');
    reccAccts.forEach(element => {
        element.classList.remove('flex-center');
    });
    
}

let reccAccts = document.querySelectorAll('.recommended-accounts');
let expandCollapse = document.querySelector('.expand-colapse');
let sidebarHead = document.querySelector('.recommended-channels-head');
function makeHorizontal() {
    sideBar.style.width = '100%';
    sideBar.style.height = '50px';
    sideBarTitle.classList.add('remove-element');
    displayName.classList.add('remove-element');
    onlineStatusViews.classList.add('remove-element');
    expandIcon.classList.add('remove-element');
    cancelSideBarBtn.classList.add('remove-element');
    sidebarTag.classList.add('remove-element');
    collapseIcon.classList.remove('remove-element');
    popularVideos.forEach((ele) => ele.classList.add('remove-element'));
    sideBar.style.float = 'none';
    sideBar2.style.float = 'none';
    sideBar2.classList.add('flex-center');
    sideBar.classList.add('flex-center');
    expandCollapse.classList.add('flex-center');
    sidebarHead.classList.add('flex-center');
    console.log(expandCollapse);
    reccAccts.forEach(element => {
        element.classList.add('flex-center');
        element.style.marginTop = '0px';
        element.style.paddingTop = '5px';
    });
    
}

collapseIcon.addEventListener('click', collapse);
expandIcon.addEventListener('click', expand);
cancelSideBarBtn.addEventListener('click', makeHorizontal);