console.log('helo world quiz')
const url = window.location.href

const quizBox = document.getElementById('quiz-box')
let data

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
/*        console.log(response)*/
        data = response.data
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)){
      /*          console.log(question)
                console.log(answers)*/
                quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>
                `
                answers.forEach(answer=>{
                    quizBox.innerHTML += `
                        <div>
                        <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                        <label for="${question}">${answer}</label>
                    `
                })
            }
        })
    },
    error: function(error){
        console.log(error)
    }
})

const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el=>{
        if (el.checked) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })

    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            // console.log(response)
            const scores = response.scores
            const results = response.results
            console.log(results)
            const rgb = ['aqua', 'black', 'blue', 'fuchsia', 'gray', 'green',
'lime', 'maroon', 'navy', 'olive', 'orange', 'purple', 'red',
'silver', 'teal', 'white', 'yellow']
            const scoreData = {
                  labels: Object.keys(scores),
                  datasets: [{
                    label: 'Gamer Motivation Dataset',
                    data: Object.values(scores),
                    backgroundColor: rgb,
                    hoverOffset: 4
                  }]
                }
            // CHART.JS CONFIG
            const config = {
              type: 'pie',
              data: scoreData,  // should be scores ,
              options: {
                responsive: true,
                plugins: {
                  legend: {
                    position: 'top',
                  },
                  title: {
                    display: true,
                    text: 'Awesome! Here are your results'
                  }
                }
              },
            }
            // END OF CHART.JS CONFIG
            quizForm.classList.add('not-visible')

            const myChart = new Chart(
                document.getElementById('scoreChart'),
                config
              )
                    // we want to display the characteristic scores only;
                    // the name of each characteristic and what the score is for each

        },
        error: function(error){
            console.log(error)
        }
    })
}

quizForm.addEventListener('submit', e=>{
    e.preventDefault()

    sendData()
})

