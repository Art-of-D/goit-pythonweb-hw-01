import logging


def get_logger():
    logging.basicConfig(
        format="%(asctime)s %(message)s",
        level=logging.DEBUG,
        handlers=[
            logging.FileHandler("program.log"),
            logging.StreamHandler(),
        ],
    )
    return logging.getLogger("logger")


logger = get_logger()

logger.info("Logger initialized and ready!")
