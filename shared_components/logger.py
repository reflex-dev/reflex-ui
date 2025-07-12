import logging

def reflex_log_level_converter(level: str) -> int:
    return logging.getLevelName(level.upper())

class ReflexLogger:
    def __init__(self, name: str, level: int):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
