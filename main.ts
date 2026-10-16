//  TerraLoop V2
//  Human in the Loop
//  micro:bit V2 - MakeCode Python
let sensor_alerta = false
let confirmacion_humana = false
function estado_normal() {
    
    sensor_alerta = false
    confirmacion_humana = false
    basic.showIcon(IconNames.Happy)
}

function evento_detectado() {
    
    sensor_alerta = true
    confirmacion_humana = false
    basic.showIcon(IconNames.Surprised)
    basic.pause(500)
    basic.showString("EVENTO")
    basic.showIcon(IconNames.Confused)
    basic.pause(500)
    basic.showString("REVISAR")
}

function alerta_roja() {
    
    confirmacion_humana = true
    basic.showIcon(IconNames.Skull)
    basic.pause(500)
    basic.showString("ROJO")
}

function alerta_critica() {
    basic.showIcon(IconNames.Skull)
    basic.pause(500)
    basic.showString("CRITICO")
    music.playTone(988, music.beat(BeatFraction.Quarter))
    music.playTone(784, music.beat(BeatFraction.Quarter))
}

//  BOTON A
//  Simula deteccion del sensor
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    if (sensor_alerta) {
        estado_normal()
    } else {
        evento_detectado()
    }
    
})
//  BOTON B
//  Primer B = confirmacion humana / ROJO
//  Segundo B = escalamiento manual / CRITICO
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    if (!sensor_alerta) {
        basic.showString("SIN EVENTO")
        basic.showIcon(IconNames.Happy)
    } else if (!confirmacion_humana) {
        alerta_roja()
    } else {
        alerta_critica()
    }
    
})
//  SHAKE
//  Simula evento ambiental detectado
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    evento_detectado()
})
//  INICIO
estado_normal()
