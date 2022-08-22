import csv


def save_record(path, timestamp, humidity, temp, darkness, lamp_state):
    with open(path, 'w', newline='') as data_file:
        writer = csv.writer(data_file, delimiter=',')
        writer.writerow([timestamp, humidity, temp, darkness, lamp_state])
        data_file.close()
