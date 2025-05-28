# Напишите программу, которая записывает в лог файл все уровни логирования: DEBUG, INFO, WARNING, ERROR, CRITICAL. 
# В каждом случае необходимо выводить соответствующее сообщение.

import logging

logging.basicConfig(
    filename='logfile.log', 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'

    )

logging.debug("This message DEBUG")
logging.info("This message INFO")
logging.warning("This message WARNING")
logging.error("This message ERROR")
logging.critical("This message CRITICAL")