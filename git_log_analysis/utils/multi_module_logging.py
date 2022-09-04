"""Logging for multiple module"""
import logging
import logging.handlers


class MultiModuleLogger:
    # class property (default : DEBUG)
    logger_names = set()
    logging_modes = {}

    @classmethod
    def set_logging_mode(cls, mode: int, target_logger_name: str) -> None:
        if type(logging.INFO) != int:
            print("[Warning] The type of mode is not 'int'")
        elif target_logger_name not in cls.logger_names:
            print(
                f"[Warning] Target logger({target_logger_name}) does not exist")
        elif mode in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
            cls.logging_modes[target_logger_name] = mode
            cls.create_logger(target_logger_name)
        else:
            print(f"[Warning] Invalid mode ({mode})")

    @classmethod
    def create_logger(cls, logger_name: str):
        # Create logger
        target_logger = logging.getLogger(logger_name)
        cls.logger_names.add(logger_name)

        # Checking if handler exists
        if target_logger.handlers:
            target_logger.setLevel(cls.logging_modes[logger_name])
            return target_logger

        cls.logging_modes[logger_name] = logging.DEBUG
        target_logger.setLevel(cls.logging_modes[logger_name])
        formatter = logging.Formatter(
            '%(asctime)s from %(name)s [%(levelname)s] %(filename)s:%(lineno)s : %(message)s')

        # Create Handlers
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(cls.logging_modes[logger_name])
        stream_handler.setFormatter(formatter)

        target_logger.addHandler(stream_handler)
        return target_logger
