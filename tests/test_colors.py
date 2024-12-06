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
