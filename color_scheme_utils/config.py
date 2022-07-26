#!/usr/bin/env python3

from pathlib import Path

kitty_default_template_conf_path = (
    Path.home() / 'testdir' / 'kitty-themes' / 'template.conf'
)
# https://github.com/kovidgoyal/kitty-themes/blob/master/template.conf


color16number_to_color_name_mapping = {
    0: 'black',
    1: 'red',
    2: 'green',
    3: 'yellow',
    4: 'blue',
    5: 'magenta',
    6: 'cyan',
    7: 'white',
}


wt_standard_key_names = {
    'black',
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white',
    'bright_black',
    'bright_red',
    'bright_green',
    'bright_yellow',
    'bright_blue',
    'bright_magenta',
    'bright_cyan',
    'bright_white',
    'cursor',
    'foreground',
    'background',
    'selection_foreground',
    'selection_background',
}

wt_standard_key_names_to_windows_terminal_key_names = {
    'cursor': 'cursorColor',
    'magenta': 'purple',
    'bright_magenta': 'brightPurple',
}

kitty_key_names_to_vscode_key_names = {
    'cursor_text_color': 'terminalCursor.background',
    'cursor': 'terminalCursor.foreground',
    'background': 'panel.background',
}
