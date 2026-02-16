import logging
import sys
from datetime import datetime

def setup_logger(name: str = "api_test", level=logging.INFO):
    
    """
    Настройка логгера для тестов
    
    Args:
        name: Имя логгера
        level: Уровень логирования
    
    Returns:
        Настроенный logger
    """""

    # Создаем logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Избегаем дублирования handlers
    if logger.handlers:
        return logger
    
    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler
    timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    file_handler = logging.FileHandler(
        f'logs/test_run_{timestamp}.log',
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# Создаем глобальный logger
logger = setup_logger()