input.onButtonPressed(Button.A, function () {
    N += 1
    basic.showNumber(N)
})
input.onButtonPressed(Button.AB, function () {
    while (true) {
        if (N >= i) {
            basic.showNumber(i ** 2)
            i += 1
        }
    }
})
input.onButtonPressed(Button.B, function () {
    N += -1
    basic.showNumber(N)
})
let N = 0
let i = 0
i = 0
