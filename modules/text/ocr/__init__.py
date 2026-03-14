"""
OCR backends: LocalOCR (Tesseract), PaddleOCRAdapter (optional, better for mixed CN/EN), Pix2TextOCR (formulas).
Data: TextBlock, OCRResult.
"""

from .base import TextBlock, OCRResult
from .local_ocr import LocalOCR
try:
    from .paddle_ocr import PaddleOCRAdapter
except ImportError:
    PaddleOCRAdapter = None
try:
    from .pix2text import Pix2TextOCR, Pix2TextBlock, Pix2TextResult
except ImportError:
    Pix2TextOCR = None
    Pix2TextBlock = None
    Pix2TextResult = None

__all__ = [
    "TextBlock",
    "OCRResult",
    "LocalOCR",
    "PaddleOCRAdapter",
    "Pix2TextOCR",
    "Pix2TextBlock",
    "Pix2TextResult",
]
