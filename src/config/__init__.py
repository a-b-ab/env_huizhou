"""
    Created by crow at 2024-12-5.
    Description: 
    Changelog: all notable changes to this file will be documented
"""

from src.utils.log_middleware import get_logger

from .config import Config

LOGGER = get_logger(Config.PROJECT_NAME)
