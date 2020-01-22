#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: BSD-3-Clause-Clear

import os
import sys
import subprocess
import shlex
# binary = input("Provide binary (including path): ")
binary = "/bin/ffmpeg"
# arguments = input("Provide arguments for that binary: ")
arguments = "-hide_banner -i %file% -c:v libx265 -preset veryslow -crf 30 -y test.mkv"
filelist = ["/path/to/file1", "/path/to/file2"]

print(binary)
print(arguments)
for i in filelist:
    x = str(binary + " " + str(arguments.replace("%file%", str('"' + str(i) + '"'))))
    x = shlex.split(x)
    print(x)
    subprocess.run(x)
    # TODO: https://stackoverflow.com/questions/10965949
