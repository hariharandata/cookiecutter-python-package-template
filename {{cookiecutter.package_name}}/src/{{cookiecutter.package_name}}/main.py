# some_module.py
import logging

from .logger.log_config import setup_logging

setup_logging()  # or setup_logging("custom/path/to/logging.yaml")


def main():
    logging.info("Starting the application...")
    # Your application logic here
    logging.info("Application finished successfully.")

if __name__ == "__main__":
    main()
    logging.info("Exiting the application.")
