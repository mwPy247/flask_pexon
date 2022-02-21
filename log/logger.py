""" The module provides basic logging capabilities. """
import logging
import os
import functools
import traceback

LOG_FILE = os.path.dirname(os.path.abspath(__file__)) + '/app.log'  # Set path to log file
FORMAT = '%(asctime)s %(message)s'  # Set format of logs


def configure_logger(log_level='info'):
    """
    The function configures the logger associated with the project.
    It sets a logging level if passed (default level 'info').

    :raises
    ValueError: Exception
    :param
    log_level: str - the logging level of the logger object associated with the project.
    :return:
    None
    """
    if log_level == 'debug':
        level = logging.DEBUG
    elif log_level == 'info':
        level = logging.INFO
    elif log_level == 'warning':
        level = logging.WARNING
    elif log_level == 'error':
        level = logging.ERROR
    elif log_level == 'critical':
        level = logging.CRITICAL
    else:
        raise ValueError("Please provide a valid log level")

    logging.basicConfig(filename=LOG_FILE, level=level, format=FORMAT)


def log_factory(level='info'):
    """
    Returns a logging decorator for implementing basic logging capabilities.


    :param
    level: str - the logging level of the logger object associated with the project.
    :return:
    log - <class 'function'> - a decorator function for logging events.
    """
    configure_logger(level)

    def log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            msg = "%s - Begin function execution with args: %s, kwargs: %s"
            logging.info(msg, func.__name__, args, kwargs)
            try:
                value = func(*args, **kwargs)
                logging.info("Returning: %s", value)
            except:
                logging.error("Exception: %s", traceback.format_exc())
                raise
            return value
        return wrapper
    return log




