# color-scheme-utils

A set of utilities for working with (terminal) color schemes / themes.

- [color-scheme-utils](#color-scheme-utils)
  - [List of utilities](#list-of-utilities)
    - [kitty-conf-extract-theme](#kitty-conf-extract-theme)
      - [Supported Output Formats](#supported-output-formats)
      - [Usage:](#usage)
  - [Installation](#installation)
    - [pipx](#pipx)
    - [pip](#pip)
  - [Thanks](#thanks)

## List of utilities

### kitty-conf-extract-theme

Extract the color settings from kitty configuration / theme files, convert them to different formats so that you can copy-paste them into the settings of your favorite terminal emulator.

#### Supported Output Formats

Click the titles to expand to see the example output generated from [kitty-theme's template.conf](https://github.com/kovidgoyal/kitty-themes/blob/master/template.conf)

<details>
  <summary>JSON</summary>

```json
{
    "foreground": "#dddddd",
    "background": "#000000",
    "selection_foreground": "#000000",
    "selection_background": "#fffacd",
    "cursor": "#cccccc",
    "cursor_text_color": "#111111",
    "url_color": "#0087bd",
    "active_border_color": "#00ff00",
    "inactive_border_color": "#cccccc",
    "bell_border_color": "#ff5a00",
    "active_tab_foreground": "#000",
    "active_tab_background": "#eee",
    "inactive_tab_foreground": "#444",
    "inactive_tab_background": "#999",
    "mark1_background": "#98d3cb",
    "mark2_background": "#f2dcd3",
    "mark3_background": "#f274bc",
    "black": "#000000",
    "bright_black": "#767676",
    "red": "#cc0403",
    "bright_red": "#f2201f",
    "green": "#19cb00",
    "bright_green": "#23fd00",
    "yellow": "#cecb00",
    "bright_yellow": "#fffd00",
    "blue": "#0d73cc",
    "bright_blue": "#1a8fff",
    "magenta": "#cb1ed1",
    "bright_magenta": "#fd28ff",
    "cyan": "#0dcdcd",
    "bright_cyan": "#14ffff",
    "white": "#dddddd",
    "bright_white": "#ffffff"
}
```

<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

<details>
  <summary>VS Code</summary>

```json
{
    "workbench.colorCustomizations": {
        "panel.background": "#000000",
        "terminalCursor.foreground": "#cccccc",
        "terminalCursor.background": "#111111",
        "terminal.ansiBlack": "#000000",
        "terminal.ansiBrightBlack": "#767676",
        "terminal.ansiRed": "#cc0403",
        "terminal.ansiBrightRed": "#f2201f",
        "terminal.ansiGreen": "#19cb00",
        "terminal.ansiBrightGreen": "#23fd00",
        "terminal.ansiYellow": "#cecb00",
        "terminal.ansiBrightYellow": "#fffd00",
        "terminal.ansiBlue": "#0d73cc",
        "terminal.ansiBrightBlue": "#1a8fff",
        "terminal.ansiMagenta": "#cb1ed1",
        "terminal.ansiBrightMagenta": "#fd28ff",
        "terminal.ansiCyan": "#0dcdcd",
        "terminal.ansiBrightCyan": "#14ffff",
        "terminal.ansiWhite": "#dddddd",
        "terminal.ansiBrightWhite": "#ffffff"
    }
}
```

<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

<details>
  <summary>Windows Terminal</summary>

```json
{
    "name": "kitty",
    "foreground": "#dddddd",
    "background": "#000000",
    "selectionForeground": "#000000",
    "selectionBackground": "#fffacd",
    "cursorColor": "#cccccc",
    "black": "#000000",
    "brightBlack": "#767676",
    "red": "#cc0403",
    "brightRed": "#f2201f",
    "green": "#19cb00",
    "brightGreen": "#23fd00",
    "yellow": "#cecb00",
    "brightYellow": "#fffd00",
    "blue": "#0d73cc",
    "brightBlue": "#1a8fff",
    "purple": "#cb1ed1",
    "brightPurple": "#fd28ff",
    "cyan": "#0dcdcd",
    "brightCyan": "#14ffff",
    "white": "#dddddd",
    "brightWhite": "#ffffff"
}
```

<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

<details>
  <summary>kitty</summary>

```
foreground                     #dddddd
background                     #000000
selection_foreground           #000000
selection_background           #fffacd
cursor                         #cccccc
cursor_text_color              #111111
url_color                      #0087bd
active_border_color            #00ff00
inactive_border_color          #cccccc
bell_border_color              #ff5a00
active_tab_foreground          #000
active_tab_background          #eee
inactive_tab_foreground        #444
inactive_tab_background        #999
mark1_background               #98d3cb
mark2_background               #f2dcd3
mark3_background               #f274bc
black                          #000000
bright_black                   #767676
red                            #cc0403
bright_red                     #f2201f
green                          #19cb00
bright_green                   #23fd00
yellow                         #cecb00
bright_yellow                  #fffd00
blue                           #0d73cc
bright_blue                    #1a8fff
magenta                        #cb1ed1
bright_magenta                 #fd28ff
cyan                           #0dcdcd
bright_cyan                    #14ffff
white                          #dddddd
bright_white                   #ffffff

```

<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

#### Usage:

```
$ kitty-conf-extract-theme -h

usage: kitty-conf-extract-theme [-h] [-V] [-c KITTY_CONF_FILE] [-f {windowsterminal,vscode,kitty,json}] [-s]

Extract the color scheme from a kitty theme / conf file

options:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -c KITTY_CONF_FILE, --kitty-conf-file KITTY_CONF_FILE, --kitty-theme-file KITTY_CONF_FILE
                        Kitty conf theme file (default: /Users/tscp/testdir/kitty-themes/template.conf)
  -f {windowsterminal,vscode,kitty,json}, --output-format {windowsterminal,vscode,kitty,json}
                        Output format (default: json)
  -s, --sort-keys       Sort color name keys (default: False)
```

## Installation

### pipx

This is the recommended installation method.

```
$ pipx install color-scheme-utils
```

### [pip](https://pypi.org/project/color-scheme-utils/)

```
$ pip install color-scheme-utils
```

## Thanks

- [Kovid Goyal]https://kovidgoyal.net) for creating kitty and it's excellent documentation.
- [vscode.one's theme editor](https://themes.vscode.one/)
