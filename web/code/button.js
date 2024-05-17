BUTTON_SIZE = 100

GREEN = '#8bc34a'
YELLOW = '#ffc107'
GREY = '#A9A9A9'

function Button(x, y) {
    this.x = x
    this.y = y

    this.current_color = 0

    this.button = createButton('')
	this.button.position(this.x - BUTTON_SIZE / 2 + 12, this.y + BUTTON_SIZE / 2 + 90)
    this.button.size(BUTTON_SIZE, BUTTON_SIZE)
    this.button.style('border', 'none')
    this.button.style('background-color', GREY)
    this.button.style('font-size', '60px')
	this.button.style('border-radius', '10px')

    this.button.mouseClicked(() => {
        this.changeColor()
    })

    this.setText = function (letter) {
        this.button.elt.innerHTML = letter
        this.current_color = 0
        this.button.style('background-color', GREY)
    }

    this.changeColor = function () {
        this.current_color += 1
        this.current_color %= 3

        if (this.current_color == 0)
            this.button.style('background-color', GREY)
        else if (this.current_color == 1)
            this.button.style('background-color', YELLOW)
        else
            this.button.style('background-color', GREEN)
    }
}
