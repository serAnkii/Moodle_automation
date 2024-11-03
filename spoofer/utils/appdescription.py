from . import logger

description = """  email-spoofer-py  
  Python 3.x based email spoofer"""

def print_description():
    logger.bright('\n{0}'.format('='*50))
    logger.header(description)
    logger.bright('{0}\n'.format('='*50))


