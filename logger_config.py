import logging

CONSOLE = logging.StreamHandler()
CONSOLE.setLevel(logging.INFO)
LOG_FILE = logging.FileHandler(".log")
LOG_FILE.setLevel(logging.WARNING)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s %(filename)s:%(lineno)d : %(message)s",
    handlers=[CONSOLE, LOG_FILE],
)

logger = logging.getLogger(__name__)
