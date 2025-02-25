"""Logging levels: kind of information we want to write to the console or file wherever we want to,
to differentiate the different kinds of actions performed by the application.
Level_1: debug (detailed info we see only debugging time)
Level_2: info (confirmation level that things are working as expected)
Level_3: warning (indication of something unexpected happened or may happen in future but software is still working as expected)
Level_4: error (software is not able to perform some functionality as expected)
Level_5: CRITICAL (program itself is unable to continue)"""

import logging

# 1-to create file that has logging levels messages
logging.basicConfig(filename="TestFile.log", level=logging.DEBUG)
logging.warning('warning message!')
logging.info('info message!')
logging.error('error message!')

# 2-to formate logging levels messages
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.DEBUG)
logging.warning('warning message!')
logging.info('info message!')
logging.error('error message!')

# 3-to get logging time
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)
logging.warning('warning message!')
logging.info('info message!')
logging.error('error message!')

# 4-to get date & time in the format we want
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    datefmt= '%d-%m-%Y %I:%M:%S %p',level=logging.DEBUG)
logging.warning('warning message!')
logging.info('info message!')
logging.error('error message!')
