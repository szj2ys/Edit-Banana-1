"""Shared utilities for processors (color, XML, image, DrawIO)."""

from .color_utils import (
    rgb_to_hex,
    hex_to_rgb,
)

from .xml_utils import (
    create_mxcell,
    create_geometry,
    prettify_xml,
    parse_drawio_xml,
)

from .image_utils import (
    calculate_iou,
)

from .drawio_library import (
    DrawIOLibrary,
    match_element_to_drawio,
    get_drawio_style,
    build_style_string,
    DRAWIO_BASIC_SHAPES,
)

__all__ = [
    'rgb_to_hex',
    'hex_to_rgb',
    'create_mxcell',
    'create_geometry',
    'prettify_xml',
    'parse_drawio_xml',
    'calculate_iou',
    'DrawIOLibrary',
    'match_element_to_drawio',
    'get_drawio_style',
    'build_style_string',
    'DRAWIO_BASIC_SHAPES',
]
