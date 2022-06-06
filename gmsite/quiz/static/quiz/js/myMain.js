console.log('beepbop')

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')
const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const time = modalBtn.getAttribute('data-time')

    modalBody.innerHTML = `
        <div class="h5 mb-3">Are you sure you want to begin "<b>${name}</b>?"</div>
        <div class="text-muted">
            <ul>
                <li>Total questions: <b>${numQuestions}</b></li>
                <li>Time: <b>${time} min</b></li>
            </ul>
    `

    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
}))