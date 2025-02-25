import logging
import Custom_Logger as CL


class CustomLoggerCall():
    log = CL.CustomLogger(logging.DEBUG)

    def method1(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method2(self):
        mthd2 = CL.CustomLogger(logging.INFO)
        mthd2.debug('debug message')
        mthd2.info('info message')
        mthd2.warning('warn message')
        mthd2.error('error message')
        mthd2.critical('critical message')


test = CustomLoggerCall()
test.method1()
test.method2()
