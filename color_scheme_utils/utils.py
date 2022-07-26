#!/usr/bin/env python3

import re
from .types import ColorScheme, WindowsTerminalColorScheme, VSCodeColorScheme
from .config import (
    color16number_to_color_name_mapping,
    wt_standard_key_names,
    wt_standard_key_names_to_windows_terminal_key_names,
    kitty_key_names_to_vscode_key_names,
)


# hex_color_pattern = r'([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})'
kitty_color_def_pattern = (
    r"(?P<name>\w+)\s+(?P<color>#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3}))\b"
)


def kitty_color_key_to_color_name(color_key: str) -> str:
    if re.match(r'color\d', color_key) or re.match(r'color1[0-5]', color_key):
        color_number = int(color_key[5:])
        if color_number in color16number_to_color_name_mapping:
            return color16number_to_color_name_mapping[color_number]
        elif color_number - 8 in color16number_to_color_name_mapping:
            return 'bright_' + color16number_to_color_name_mapping[color_number - 8]
        else:
            return color_key
    else:
        return color_key


def kitty_conf_extract_theme(content: str) -> ColorScheme:
    """_summary_:

    Args:
        content (str): content of the kitty conf / theme file

    Returns:
        COLOR_SCHEME: color scheme dict
    """
    theme_dict = {
        kitty_color_key_to_color_name(name): color
        for name, color, _ in re.findall(kitty_color_def_pattern, content)
    }
    return theme_dict


def color_scheme_to_windows_terminal(
    color_scheme: ColorScheme, color_scheme_name: str | None = 'kitty'
) -> WindowsTerminalColorScheme:
    from stringcase import camelcase

    wt_dict = {}
    if color_scheme_name is not None:
        wt_dict['name'] = color_scheme_name
    for name, color in color_scheme.items():
        if name not in wt_standard_key_names:
            continue
        if name in wt_standard_key_names_to_windows_terminal_key_names:
            wt_name = wt_standard_key_names_to_windows_terminal_key_names[name]
        else:
            wt_name = camelcase(name)
        wt_dict[wt_name] = color
    return wt_dict


def color_scheme_to_vscode(
    color_scheme: ColorScheme,
) -> VSCodeColorScheme:
    from stringcase import camelcase, pascalcase

    possible_colors_in_color_scheme = set()
    for color in color16number_to_color_name_mapping.values():
        possible_colors_in_color_scheme.add(color)
        possible_colors_in_color_scheme.add('bright_' + color)
    vsc_dict = {}
    for name, color in color_scheme.items():
        if name in possible_colors_in_color_scheme:
            vsc_dict[f'terminal.ansi{pascalcase(name)}'] = color
            continue
        if name in kitty_key_names_to_vscode_key_names:
            vsc_name = kitty_key_names_to_vscode_key_names[name]
            vsc_dict[vsc_name] = color

    return {'workbench.colorCustomizations': vsc_dict}


def color_scheme_to_kitty(color_scheme: ColorScheme, sort_key: bool = False) -> str:
    # kitty_color_defs: list[str] = []
    kitty_color_defs = [f'{name:30} {color}' for name, color in color_scheme.items()]
    if sort_key:
        lines = sorted(kitty_color_defs)
    else:
        lines = kitty_color_defs
    return '\n'.join(lines)
