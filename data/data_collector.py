import datetime
import file_manager

PATH = "./data/"


class DataCollector:

    def __init__(self):
        self.file_timestamp = datetime.date.today()
        self.file_path = "{}{}.csv".format(PATH, self.file_timestamp)

    def save_status(self, humidity, temp, darkness, lamp_state):
        timestamp = datetime.datetime.strftime("%d-%m-%Y %H:%M")
        file_manager.save_record(self.file_path, timestamp, humidity, temp, darkness, lamp_state)

    def check_file(self):
        if self.file_timestamp != datetime.date.today() and datetime.datetime.strftime("%A") == "Monday":
            self.file_timestamp = datetime.date.today()
            self.file_path = "{}{}.csv".format(PATH, self.file_timestamp)
