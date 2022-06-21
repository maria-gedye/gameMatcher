const url = window.location.href
console.log(url)
const homeBtn = document.getElementById('home-button')

homeBtn.addEventListener('click', ()=>{
        homeUrl = window.location.href.slice(0, -2)
        window.location.href = homeUrl
    })