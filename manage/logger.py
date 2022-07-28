import logging
import time

log_format = '%(asctime)s  %(name)8s  %(levelname)5s  %(message)s'
timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ")
filename = "./log/test_{}.log".format(timestamp)


def get_logger(name):
    logging.basicConfig(level=logging.DEBUG,
                        format=log_format,
                        filename=filename,
                        filemode='w')
    return logging.getLogger(name)
