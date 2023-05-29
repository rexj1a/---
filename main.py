def on_button_pressed_a():
    global N
    N += 1
    basic.show_number(N)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global i
    while True:
        if N >= i:
            basic.show_number(i ** 2)
            i += 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global N
    N += -1
    basic.show_number(N)
input.on_button_pressed(Button.B, on_button_pressed_b)

N = 0
i = 0
i = 0