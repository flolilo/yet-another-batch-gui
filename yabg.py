#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: BSD-3-Clause-Clear OR GPL-3.0-only
"""yet-another-batch-gui - Yet another batch GUI. Inspired by AnotherGUI, scripted in Python."""
__author__ = "flolilo"
__license__ = "See SPDX-License-Identifier"
__contact__ = "See github.com/flolilo/yet-another-batch-gui"
__version__ = "0.0.1"

# import os
# import sys
import subprocess
import shlex
from pathlib import Path
from ruamel.yaml import YAML
yaml = YAML()
yaml.indent(offset=2, sequence=4)

# binary = input("Provide binary (including path): ")
all_presets = {
    'binaries': [str(Path("/bin/ffmpeg").resolve()),
                 str(Path("/bin/ffprobe").resolve())],
    'presets': ["bla\ %2", 'asd', '##1'],
    'settings': {
        'threads': 4
    }
}

with Path('./yabg.yaml').open('r+', encoding='utf-8') as file:
    yaml.dump(all_presets, file)
# arguments = input("Provide arguments for that binary: ")
arguments = "-hide_banner -i %file% -c:v libx265 -preset veryslow -crf 30 -y test.mkv"
filelist = ["/path/to/file1", "/path/to/file2"]

"""
print(binary)
print(arguments)
for i in filelist:
    x = str(binary + " " + str(arguments.replace("%file%", str('"' + str(i) + '"'))))
    x = shlex.split(x)
    print(x)
    subprocess.run(x)
    # TODO: https://stackoverflow.com/questions/10965949
"""
