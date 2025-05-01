# CHANGELOG

## v1.0.2

- Changed: `WColors.luminance_color` method know accept only `ColorValue|WColors` and return `str`
- Fixed: `WColors.luminance` when enter `Enum` value
- Fixed: `WColors.luminance` 'is not a valid color' error

## v1.1.0

- Changed: `WColors.luminance` has been renamed to `WColors.luminance_value`
- Added: `WColors.rgb` property value.
- Added: `WColors.luminance` property value.
- Added: `WColors + opacity` to add opacity to the color value.

## v1.1.2

- Added: `rgb_to_hex`, `mix_colors`, `mix_dark`, `mix_light` methods