from manage import gpio_manager


class LightSensor:
    def __init__(self, name, gpio_pin):
        self.name = name
        self.gpio_pin = gpio_pin

    def get_status(self):
        status = gpio_manager.read_state(self.gpio_pin)
        return status
