#!/usr/bin/env python3

from typing import Literal

ColorScheme = dict[str, str]
WindowsTerminalColorScheme = dict[str, str]
VSCodeColorScheme = dict[Literal['workbench.colorCustomizations'], dict[str, str]]
