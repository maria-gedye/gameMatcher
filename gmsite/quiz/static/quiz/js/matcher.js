console.log('helo world matcher')
const url = window.location.href

let data
// this takes JsonResponse from game_data_view and can be used in html
$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        console.log(response)
        // put in table syntax below to display each game
        /*data = response.data
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)){
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
    },*/
    error: function(error){
        console.log(error)
    }
})