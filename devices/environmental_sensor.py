import logging
import time

import dht11

logging.basicConfig(filename="log.txt", level=logging.INFO)
logger = logging.getLogger("environmental_sensor")


class EnvironmentalSensor:
    def __init__(self, name, gpio_pin, limit):
        self.sensor = None
        self.name = name
        self.limit = limit
        self.sensor = dht11.DHT11(pin=gpio_pin)

    def read_data(self, counter):
        counter += 1

        result = self.sensor.read()
        humidity = result.humidity
        temp = result.temperature

        if humidity == 0 and temp == 0 and counter < self.limit:
            time.sleep(1)
            return self.read_data(counter)

        return humidity, temp

    def get_data(self):
        humidity, temp = self.read_data(counter=0)
        return humidity, temp
