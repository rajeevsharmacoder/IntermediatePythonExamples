import logging
from logging.hanlders import RotatingFileHandler, TimedRotatingFileHandler
import time
# import logging.config

# logging.config.fileConfig('logging.conf')
# import helper
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(messsage)s', datefmt="%Y%m%d %H:%M:%S")
# logging.debug('Debug Message')
# logging.info('Info Message')
# logging.warning('Warning Message')
# logging.error('Error Message')
# logging.critical('Critical Message')

# logger = loggin.getLogger(__name__)

# stream_handler = logging.StreamHandler()
# file_handler = loggin.FileHandler('file.log')

# # level and format to be set for each handler
# stream_handler.setLevel(logging.WARNING)
# file_handler.setLevel(logging.ERROR)
# stream_formatter = logging.Formatter('%(name)s - %(levelname)s - %(messsage)s')
# file_formatter = logging.Formatter('%(name)s - %(levelname)s - %(messsage)s')

# stream_handler.setFormatter(stream_formatter)
# file_handler.setFormatter(file_formatter)

# logger.addHandler(stream_handler)
# logger.addHandler(file_handler)

# logger.warning('This is a warning !!')
# logger.error('This is an error !!')

# logger = logging.getLogger('simpleExample')
# logger.debug('This is a debug message')

# try:
#     a = [1, 2, 3]
#     val = a[4]
# except IndexError as e:
#     logging.error(e, exc_info=True)
# import traceback

# try:
#     a = [1, 2, 3]
#     val = a[4]
# except:
#     logging.error('The error is %s', traceback.format_exc())


# Rotating file handler
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

# for _ in range(10000):
#     logger.info('Hello World!!')


# # Timed Rotating
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # s, m, h, d, mignight, w0
# handler = TimedRotatingFileHandler(
#     'timed_test.log', when='s', interval=5, backupCount=5)
# logger.addHandler(handler)

# for _ in range(6):
#     logger.info('Hello World!!')
#     time.sleep(5)


# Search for python json logger on github
