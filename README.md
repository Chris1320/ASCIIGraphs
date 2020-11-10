# ASCIIGraphs

## Description

Create neat loading screens on consoles using Python.

## Example Usage

```Python

from asciigraphs import ASCIIGraphs

waiting_time = 3
description = "Please wait for your turn..."

ASCIIGraphs().progress_bar(waiting_time, description)

```

```Python

import time
from asciigraphs import ASCIIGraphs

lines_to_write = (
    "Hello,",
    "World!"
    "The universe",
    "Is huge!"
)
i = 0
filename = "hello.txt"

with open(filename, 'a') as f:
    while i < len(lines_to_write):
        ASCIIGraphs().progress_bar_manual("Writing to file...", i, len(lines_to_write))
        f.write(lines_to_write[i] + '\n')
        time.sleep(3)

```
