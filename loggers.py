import logging
# Create a custom logger
logger = logging.getLogger(__name__)
# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)
# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)
# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)
logger.warning('This is a warning')
logger.error('This is an error')

logger.debug("this is basic information")
logger.info("this is basic information")


def meeting():
    print("hello")
    logger.info("Meeting was successful")


def introducing():
    meeting()
    a = "my name is Elnar"
    print(a)
    logger.info("introducing was successful")


def asking():
    introducing()
    b = "How are you?"
    try:
        if b == "How are you?":
            print(b)
            return "OK"
        else:
            raise ValueError
    except ValueError as e:
        print(e)
        logger.critical("Critical Error")


print(asking())
