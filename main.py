# TerraLoop V2
# Human in the Loop
# micro:bit V2 - MakeCode Python

sensor_alerta = False
confirmacion_humana = False


def estado_normal():
    global sensor_alerta, confirmacion_humana

    sensor_alerta = False
    confirmacion_humana = False

    basic.show_icon(IconNames.HAPPY)


def evento_detectado():
    global sensor_alerta, confirmacion_humana

    sensor_alerta = True
    confirmacion_humana = False

    basic.show_icon(IconNames.SURPRISED)
    basic.pause(500)

    basic.show_string("EVENTO")

    basic.show_icon(IconNames.CONFUSED)
    basic.pause(500)

    basic.show_string("REVISAR")


def alerta_roja():
    global confirmacion_humana

    confirmacion_humana = True

    basic.show_icon(IconNames.SKULL)
    basic.pause(500)

    basic.show_string("ROJO")


def alerta_critica():
    basic.show_icon(IconNames.SKULL)
    basic.pause(500)

    basic.show_string("CRITICO")

    music.play_tone(988, music.beat(BeatFraction.QUARTER))
    music.play_tone(784, music.beat(BeatFraction.QUARTER))


# BOTON A
# Simula deteccion del sensor

def on_button_pressed_a():
    if sensor_alerta:
        estado_normal()
    else:
        evento_detectado()

input.on_button_pressed(Button.A, on_button_pressed_a)


# BOTON B
# Primer B = confirmacion humana / ROJO
# Segundo B = escalamiento manual / CRITICO

def on_button_pressed_b():

    if not sensor_alerta:
        basic.show_string("SIN EVENTO")
        basic.show_icon(IconNames.HAPPY)

    elif not confirmacion_humana:
        alerta_roja()

    else:
        alerta_critica()

input.on_button_pressed(Button.B, on_button_pressed_b)


# SHAKE
# Simula evento ambiental detectado

def on_gesture_shake():
    evento_detectado()

input.on_gesture(Gesture.SHAKE, on_gesture_shake)


# INICIO

estado_normal()
