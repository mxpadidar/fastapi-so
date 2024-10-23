import logging


class Logger:
    __instance: "Logger | None" = None
    __logger: logging.Logger

    def __new__(cls, name: str) -> "Logger":
        if cls.__instance is not None:
            return cls.__instance

        cls.__instance = super(Logger, cls).__new__(cls)
        cls.__instance._initialize(name)
        return cls.__instance

    def _initialize(self, name: str) -> None:
        self.__logger = logging.getLogger(name)
        self.__logger.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.__logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Logs an info message."""
        self.__logger.info(message)

    def error(self, message: str) -> None:
        """Logs an error message."""
        self.__logger.error(message)
