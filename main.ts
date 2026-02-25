let steps = 0
input.onButtonPressed(Button.A, function () {
    steps = 0
})
input.onGesture(Gesture.Shake, function () {
    steps += 1
})
basic.forever(function () {
    basic.showNumber(steps)
})
