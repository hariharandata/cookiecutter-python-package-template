# some_module.py
from .logger.log_config import setup_logging
import logging

setup_logging()  # or setup_logging("custom/path/to/logging.yaml")

logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Info message")