"""
DrawIO shape library and style helpers. Used by other modules (arrows handled as icons).
"""

from typing import Any

# ---------- DrawIO shape names ----------
DRAWIO_BASIC_SHAPES = [
    "rectangle", "ellipse", "rhombus", "triangle", "hexagon", "parallelogram", "cylinder",
]


class DrawIOLibrary:
    """DrawIO shape library (placeholder for extension)."""
    pass


def build_style_string(**attrs: Any) -> str:
    """Convert style dict to DrawIO style string."""
    return ";".join(f"{k}={v}" for k, v in attrs.items() if v is not None)


def get_drawio_style(element_type: str, **overrides: Any) -> str:
    """Default DrawIO style by shape type (overridable)."""
    base = {"shape": "rectangle", "strokeColor": "#000000", "fillColor": "#ffffff"}
    base.update(overrides)
    return build_style_string(**base)


def match_element_to_drawio(element_type: str) -> str:
    """Map internal type to DrawIO shape name."""
    m = {"rectangle": "rectangle", "ellipse": "ellipse", "triangle": "triangle", "arrow": "connector"}
    return m.get(element_type.lower(), "rectangle")
