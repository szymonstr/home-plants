import RPi.GPIO as GPIO

LIGHT_SENSOR = 7
LAMP_RELAY = 16


def get_light_sensor_pin():
    return LIGHT_SENSOR


def get_lamp_relay_pin():
    return LAMP_RELAY


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LIGHT_SENSOR, GPIO.IN)
    GPIO.setup(LAMP_RELAY, GPIO.OUT)


def read_state(pin):
    status = GPIO.input(pin)
    return status


def set_state(pin, state):
    GPIO.output(pin, state)


def cleanup_GPIO():
    GPIO.cleanup()
