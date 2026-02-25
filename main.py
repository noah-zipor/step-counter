steps = 0

def on_button_pressed_a():
    global steps
    steps = 0
    basic.show_number(steps)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global steps
    steps += 1
    basic.show_number(steps)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
