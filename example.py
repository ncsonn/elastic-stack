import logging

from logstash import TCPLogstashHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("logstash")

console_handler = logging.StreamHandler()
handler = TCPLogstashHandler(host="localhost", port=5002, version=1)

logger.addHandler(handler)
logger.addHandler(console_handler)

logger.info("Hello, Logstash!")
logger.error("This is an error message")
logger.warning("This is a warning message")
