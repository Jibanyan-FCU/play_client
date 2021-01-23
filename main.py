# send number 1 if button A is pressed
def on_button_pressed_a():
    global lock, number
    if not (lock):
        number = 1
        music.play_tone(Note.C, music.beat(1))
        radio.send_number(1)
        lock = True
input.on_button_pressed(Button.A, on_button_pressed_a)

# send number 2 if button B is pressed
def on_button_pressed_b():
    global lock, number
    if not (lock):
        number = 2
        music.play_tone(Note.C, music.beat(1))
        radio.send_number(2)
        lock = True
input.on_button_pressed(Button.B, on_button_pressed_b)

# send number 3 if button A and B are pressed
def on_button_pressed_ab():
    global lock, number
    if not (lock):
        number = 3
        music.play_tone(Note.C, music.beat(1))
        radio.send_number(3)
        lock = True
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# get the result from server
def on_received_string(receivedString):
    global lock
    if receivedString == "true":
        basic.show_icon(IconNames.YES)
    elif receivedString == "false":
        basic.show_icon(IconNames.NO)
    else:
        basic.show_string("Error: Unknown received string.")
    lock = False
radio.on_received_string(on_received_string)

number = 0
lock = False
radio.set_group(5)

def on_forever():
    if lock:
        basic.show_number(number)
basic.forever(on_forever)
