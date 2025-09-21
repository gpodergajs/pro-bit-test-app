import logging

def get_logger(name: str) -> logging.Logger:
    """
    Returns a logger instance with the specified name.

    Args:
        name (str): The name of the logger, typically __name__ of the calling module.

    Returns:
        logging.Logger: A logger instance.
    """