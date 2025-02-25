import logging

class LoggerDemoConsole():

    def testLog(self):
        # create logger
        # logger = logging.getLogger("SampleLog")
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        # create console handler and give it a level
        Console_Handler = logging.StreamHandler()
        Console_Handler.setLevel(logging.INFO)

        # create formatter
        Formatter = logging.Formatter('%(asctime)s -%(name)s- %(levelname)s : %(message)s',
                                      datefmt='%d-%m-%Y %I:%M:%S %p')

        # add formatter to the handler
        Console_Handler.setFormatter(Formatter)

        # add consoler_handler to the logger
        logger.addHandler(Console_Handler)

        # logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')


demo = LoggerDemoConsole()
demo.testLog()
