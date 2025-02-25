import logging
import inspect

def CustomLogger(logLevel):
    # Gets the name of the class or method from where this method is called
    LoggerName = inspect.stack()[1][3]
    Logger = logging.getLogger(LoggerName)

    # By default, log all messages
    Logger.setLevel(logging.DEBUG)

    # define a file handler
    File_Handler = logging.FileHandler(filename='{0}.log'.format(LoggerName), mode='w')
    File_Handler.setLevel(logLevel)

    # define format
    Formatter = logging.Formatter('%(asctime)s -%(name)s- %(levelname)s : %(message)s',
                                      datefmt='%d-%m-%Y %I:%M:%S %p')
    # define format of the handler
    File_Handler.setFormatter(Formatter)
    # add handler to the logger
    Logger.addHandler(File_Handler)

    return Logger

