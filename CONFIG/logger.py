import logging

log_file_path = 'log_file.log'
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

logger = logging.getLogger(__name__) #Allow us to work with different log classes
logger.setLevel(logging.DEBUG)
logger.propagate = False

log_info = logging.StreamHandler()
log_info.setLevel(logging.INFO)
logger.addHandler(log_info)

fh = logging.FileHandler(log_file_path, 'w+')
fh.setFormatter(formatter)
logger.addHandler(fh)