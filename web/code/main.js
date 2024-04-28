let BUTTONS_NUMBER = 5;
let buttons = [];

function generateToken(n) {
    var chars = 'abcdefghijklmnopqrstuvwxyz0123456789';
    var token = '';
    for (var i = 0; i < n; i++) {
        token += chars[Math.floor(Math.random() * chars.length)];
    }
    return token;
}

let TOKEN = ''

function setup() {
    // createCanvas(window.innerWidth, window.innerHeight);

    for (var i = 0; i < BUTTONS_NUMBER; i += 1) {
        buttons.push(new Button(window.innerWidth / 2 - ((BUTTONS_NUMBER - 1) / 2 - i) * (BUTTON_SIZE + 10), window.innerHeight / 2))
    }

    let button = createButton('Отправить ответ')
    button.position(window.innerWidth / 2 - button.width / 2, window.innerHeight / 2 + BUTTON_SIZE / 2 + 20)
    button.mouseClicked(() => {
        playGame()
    })

    background(250)

    if (document.cookie.length == 0) {
        document.cookie = generateToken(20)
    }

    TOKEN = document.cookie

    restartGame()
}

function keyPressed(key) {
    if (1 <= key.key && key.key <= BUTTONS_NUMBER) {
        buttons[key.key - 1].changeColor();
    }
    if (key.key == 'Enter') {
        playGame()
    }
}