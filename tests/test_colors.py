import flet as ft
from flet_wcolors import WColors


def test_web_colors_random_with_weights_and_exclude():
    """Test random material color selection with weights and exclusion list."""
    results = [
        WColors.random(
            exclude=[WColors.RED],
            weights={WColors.BLUE: 150},
        )
        for _ in range(1000)
    ]
    assert WColors.RED not in results
    assert WColors.BLUE in results


def test_hex_to_rgb():
    # WHITE color
    r = WColors.hex_to_rgb("#ffffff")
    assert r == (255,) * 3

    # BLACK color
    r = WColors.hex_to_rgb("#000000")
    assert r == (0,) * 3

    # RED color
    r = WColors.hex_to_rgb("#FF0000")
    assert r == (255, 0, 0)


def test_luminance_methods():
    r = WColors.luminance_value("BLACK")
    assert r < 0.5

    r = WColors.luminance_value(ft.Colors.BLACK)
    assert r < 0.5

    r = WColors.luminance_value("WHITE")
    assert r > 0.5

    r = WColors.luminance_value(ft.Colors.WHITE)
    assert r > 0.5

    r = WColors.luminance_color(ft.Colors.WHITE)
    assert r == "#000000"

    r = WColors.luminance_color(ft.Colors.BLACK)
    assert r == "#ffffff"


def test_rgb_property():
    # RED color
    r = WColors.RED.rgb
    assert r == (255, 0, 0)

    # WHITE color
    r = WColors.WHITE.rgb
    assert r == (255, 255, 255)


def test_luminance_property():
    # BLACK color
    r = WColors.BLACK.luminance
    assert r < 0.5

    # WHITE color
    r = WColors.WHITE.luminance
    assert r > 0.5


def test_add_expr():
    # BLACK color
    r = WColors.BLACK + 0.5
    assert r == "#000000,0.5"

    # WHITE color
    r = WColors.WHITE + 0.3
    assert r == "#FFFFFF,0.3"
