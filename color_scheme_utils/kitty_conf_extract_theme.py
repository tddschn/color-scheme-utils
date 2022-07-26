#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-07-26
Purpose: Extract the color scheme from a kitty theme / conf file
"""

import argparse
import json
from pathlib import Path
from . import __version__
from .config import kitty_default_template_conf_path
from .utils import (
    kitty_conf_extract_theme,
    color_scheme_to_windows_terminal,
    color_scheme_to_vscode,
    color_scheme_to_kitty,
)


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Extract the color scheme from a kitty theme / conf file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        '-V',
        '--version',
        action='version',
        version=f'%(prog)s {__version__}',
    )

    parser.add_argument(
        '-c',
        '--kitty-conf-file',
        '--kitty-theme-file',
        type=Path,
        default=str(kitty_default_template_conf_path),
        help='Kitty conf theme file',
    )

    parser.add_argument(
        '-f',
        '--output-format',
        choices=['windowsterminal', 'vscode', 'kitty', 'json'],
        default='json',
        help='Output format',
    )

    parser.add_argument(
        '-s', '--sort-keys', action='store_true', help='Sort color name keys'
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    conf_file = args.kitty_conf_file
    if not conf_file.exists():
        print(f'{conf_file} does not exist')
        return

    theme_dict = kitty_conf_extract_theme(conf_file.read_text())
    output_dict = None
    output_format = args.output_format
    match output_format:
        case 'json':
            output_dict = theme_dict
        case 'windowsterminal':
            output_dict = color_scheme_to_windows_terminal(theme_dict)
        case 'vscode':
            output_dict = color_scheme_to_vscode(theme_dict)
        case 'kitty':
            print(color_scheme_to_kitty(theme_dict, sort_key=args.sort_keys))
            return

    if args.sort_keys:
        assert output_dict is not None
        output_dict = {k: v for k, v in sorted(output_dict.items(), key=lambda x: x[0])}

    print(json.dumps(output_dict, indent=4))


if __name__ == '__main__':
    main()
