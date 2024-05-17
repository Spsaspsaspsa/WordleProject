let API_URL = 'http://127.0.0.1:8000'

function restartGame() {
    loadJSON(API_URL + '/play?token=' + TOKEN, processRequest)
}

function playGame() {
    var test = getCurrentWord()
    var mark = getButtonsState()
    loadJSON(API_URL + '/play?token=' + TOKEN + '&test=' + test + '&mark=' + mark, processRequest)
}

function getButtonsState() {
    var result = ''
    for (var i = 0; i < BUTTONS_NUMBER; i += 1) {
        result += str(buttons[i].current_color)
    }
    return result
}

function getCurrentWord() {
    var result = ''
    for (var i = 0; i < BUTTONS_NUMBER; i += 1) {
        result += buttons[i].button.elt.innerHTML
    }
    return result
}

function processRequest(js) {
    if (js['status'] == 'answer') {
        // alert('Я думаю слово: ' + js['word'])
        Swal.fire({
            title: js['word'],
            text: "Я угадал слово, которое Вы загадали :)",
            icon: "success"
        })
        restartGame()
    } else if (js['status'] == 'fail') {
        Swal.fire({
            title: "Ошибка",
            text: "Я не знаю слова, которое Вы загадали :(",
            icon: "error"
        })
        restartGame()
    } else {
        for (var i = 0; i < BUTTONS_NUMBER; i += 1) {
            buttons[i].setText(js['word'][i])
        }
    }
}