### python-packages
import logging
from logging.handlers import RotatingFileHandler
import sys
from pathlib import Path
import os

class LoggerSetup():
    def __init__(self, log_name='api.log', max_megabytes=10, backup_count=1, log_to_console=True):
        self.log_name = log_name
        self.log_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), f'../../../log/{self.log_name}')
        Path(self.log_file).touch(exist_ok=True) # create file if file does not exist
        
        self.max_bytes = int(1048576 * max_megabytes)
        self.backup_count = backup_count
        self.log_to_console = log_to_console

    def setup_logger(self):
        """
            Initialize Handlers
        """
        logging.getLogger(self.log_name).setLevel(logging.INFO)
        logging.getLogger(self.log_name).addHandler(self.rotating_log_handler()) # add a rotating log handler
        
        if self.log_to_console:
            logging.getLogger(self.log_name).addHandler(self.console_log_handler())  # add a console log handler
        
        return logging.getLogger(self.log_name)
    
    def get_logger(self):
        """
            Returns an Initialized logger object
        """
        return self.setup_logger()

    def rotating_log_handler(self):
        """
            Handler for setting up rotating log file
        """
        logHandler = RotatingFileHandler(self.log_file, maxBytes=self.max_bytes, backupCount=self.backup_count, mode='a')
        logHandler.setLevel(logging.INFO)
        logFormatter = logging.Formatter('%(asctime)s.%(msecs)03d [%(filename)-15.15s:%(lineno)-3.3d] [%(levelname)-4.4s] %(message)s', 
            datefmt='%m-%d-%Y %H:%M:%S')
        logHandler.setFormatter(logFormatter)
        return logHandler

    def console_log_handler(self):
        """
            Handler for logging to console
        """
        stdoutHandler = logging.StreamHandler(sys.stdout)
        stdoutHandler.setLevel(logging.INFO)
        stdoutFormatter = logging.Formatter('[%(levelname)-4.4s] [%(asctime)s] %(message)s', 
            datefmt='%H:%M:%S')
        stdoutHandler.setFormatter(stdoutFormatter)
        return stdoutHandler


if __name__ == "__main__":
    # test messages
    log = LoggerSetup().get_logger()
    log.debug(f"Test - Harmless debug Message")
    log.info("Test - Just an information")
    log.warning("Test - Its a Warning")
    log.error("Test - Did you try to divide by zero")
    log.critical("Test - Internet is down")
    log.exception("Test - Exception")