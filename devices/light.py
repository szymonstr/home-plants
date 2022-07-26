from gpio import gpio_manager
import logging

logging.basicConfig(filename="log.txt", level=logging.INFO)
logger = logging.getLogger("light")


class Lamp:
    def __init__(self, name, gpio_pin, state):
        self.name = name
        self.gpio_pin = gpio_pin
        self.state = state

    def setup(self):
        if self.state == 0:
            self.switch_on()
        else:
            self.switch_off()

    def switch_on(self):
        gpio_manager.set_state(self.gpio_pin, 0)
        self.state = 0
        logger.info("Switch on lamp: {}".format(self.name))

    def switch_off(self):
        gpio_manager.set_state(self.gpio_pin, 1)
        self.state = 1
        logger.info("Switch off lamp: {}".format(self.name))
