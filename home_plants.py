from gpio import gpio_manager
from devices import light, light_sensor, environmental_sensor
import timer

import time
import logging

logging.basicConfig(filename="log.txt", level=logging.INFO)
logger = logging.getLogger("home_plants")


def switch_on_lights(lamp):
    if lamp.state == 1:
        lamp.switch_on()


def switch_off_lights(lamp):
    if lamp.state == 0:
        lamp.switch_off()


def manage_illumination(lamp, light_detector):
    darkness = light_detector.get_status()
    logger.info("Darkness: {}".format(darkness))
    logger.info("Lamp state: {}".format(lamp.state))
    if timer.get_status():
        if darkness:
            switch_on_lights(lamp)
        else:
            switch_off_lights(lamp)
    else:
        switch_off_lights(lamp)


def environment_status(env_sensor):
    humidity, temp = env_sensor.get_data()
    logger.info("Temperature: {}*C Humidity: {}%".format(temp, humidity))


def switch_on_heating():
    return 0


def switch_off_heating():
    return 0


def main():

    logger.info("Start program!")
    gpio_manager.setup()

    env_name = 'E1'
    init_state = 1
    logger.info("Environment name set: {}".format(env_name))
    logger.info("Lamp initial state set: ".format(init_state))
    lamp_pin = gpio_manager.LAMP_RELAY
    lamp = light.Lamp(env_name, lamp_pin, init_state)
    lamp.setup()

    light_sensor_pin = gpio_manager.LIGHT_SENSOR
    light_detector = light_sensor.LightSensor(env_name, light_sensor_pin)

    env_sensor_limit = 5
    env_sensor_pin = gpio_manager.get_environment_sensor_pin()
    env_sensor = environmental_sensor.EnvironmentalSensor(env_name, env_sensor_pin, env_sensor_limit)

    while(True):
        manage_illumination(lamp, light_detector)
        environment_status(env_sensor)
        time.sleep(15 * 60)


if __name__ == "__main__":
    main()
