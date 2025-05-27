import logging
import sys
from logging import Logger

class Color:
    """Kelas untuk menyimpan kode warna ANSI untuk terminal."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ColoredFormatter(logging.Formatter):
    """
    Formatter kustom untuk menambahkan warna pada output log berdasarkan level.
    """
    def __init__(self, fmt: str):
        super().__init__(fmt)
        self.FORMATS = {
            logging.DEBUG: f"{Color.CYAN}{fmt}{Color.END}",
            logging.INFO: f"{Color.BLUE}{fmt}{Color.END}",
            logging.WARNING: f"{Color.YELLOW}{fmt}{Color.END}",
            logging.ERROR: f"{Color.RED}{fmt}{Color.END}",
            logging.CRITICAL: f"{Color.BOLD}{Color.RED}{fmt}{Color.END}",
            logging.SUCCESS: f"{Color.GREEN}{fmt}{Color.END}"
        }
    
    def format(self, record: logging.LogRecord) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
    
def setup_logger(verbose: bool = False) -> Logger:
    """
    Mengonfigurasi dan mengembalikan instance logger.

    Args:
        verbose (bool): Jika True, level log diatur ke DEBUG.

    Returns:
        Logger: Instance logger yang telah dikonfigurasi.
    """
    logging.SUCCESS = 25
    logging.addLevelName(logging.SUCCESS, "SUKSES")

    logger = logging.getLogger("VideqDownloader")

    if logger.hasHandlers():
        logger.handlers.clear()
    
    level = logging.DEBUG if verbose else logging.INFO
    logger.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)

    log_format = "[%(asctime)s] [%(levelname)-8s] %(message)s"
    formatter = ColoredFormatter(log_format)
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    def success(self, message, *args, **kws):
        if self.isEnabledFor(logging.SUCCESS):
            self._log(logging.SUCCESS, message, args, **kws)
    
    logger.success = success.__get__(logger, logging.Logger)

    return logger