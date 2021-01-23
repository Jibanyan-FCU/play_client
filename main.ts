//  send number 1 if button A is pressed
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (!lock) {
        number = 1
        music.playTone(Note.C, music.beat(1))
        radio.sendNumber(1)
        lock = true
    }
    
})
//  send number 2 if button B is pressed
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (!lock) {
        number = 2
        music.playTone(Note.C, music.beat(1))
        radio.sendNumber(2)
        lock = true
    }
    
})
//  send number 3 if button A and B are pressed
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    if (!lock) {
        number = 3
        music.playTone(Note.C, music.beat(1))
        radio.sendNumber(3)
        lock = true
    }
    
})
//  get the result from server
radio.onReceivedString(function on_received_string(receivedString: string) {
    
    lock = false
    if (receivedString == "true") {
        basic.showIcon(IconNames.Yes)
    } else if (receivedString == "false") {
        basic.showIcon(IconNames.No)
    } else {
        basic.showString("Error: Unknown received string.")
    }
    
})
let number = 0
let lock = false
radio.setGroup(5)
basic.forever(function on_forever() {
    if (lock) {
        basic.showNumber(number)
    }
    
})
