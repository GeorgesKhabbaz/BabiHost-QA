"""Utility for setting up application logging."""
import logging
import os

def setup_logger(name):
    """
    Set up and return a logger that writes to logs/test.log.
    """
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(os.path.join(log_dir, "test.log"))
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
