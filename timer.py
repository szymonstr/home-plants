from datetime import datetime

START_HOUR = 12
START_MINUTE = 00
STOP_HOUR = 20
STOP_MINUTE = 00


def get_start_time():
    start_time = START_HOUR*60 + START_MINUTE
    return start_time


def get_end_time():
    end_time = STOP_HOUR*60 + STOP_MINUTE
    return end_time


def get_current_time():
    current_time = datetime.now().hour * 60 + datetime.now().minute
    return current_time


def calculate_status():

    if get_start_time() <= get_current_time() <= get_end_time():
        return True

    return False


def get_status():
    status = calculate_status()
    return status
