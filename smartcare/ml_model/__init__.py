"""
Smart Care - ML Model Package
Plant Disease Detection and Remedy System
"""

__version__ = '1.0.0'
__author__ = 'Smart Care Team'

# Expose main functions for easy imports
from .disease_predictor import get_predictor
from .disease_remedies import get_remedy, format_remedy_text

__all__ = [
    'get_predictor',
    'get_remedy',
    'format_remedy_text'
]