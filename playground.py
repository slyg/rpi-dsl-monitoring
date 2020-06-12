#!/usr/bin/env python3

import os
import random
import signal
import sys
from time import sleep

from icons import (demon, fantom_blue_md, fantom_blue_tl, fantom_red_tl,
                   fantom_red_tr, skull, skull_front,
                   skull_front_red, bender, ghost, green_ghost, pumpkin, creeper)
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(270)


def exit_handler(signal):
    sense.clear()
    sys.exit(0)


signal.signal(signal.SIGTERM, exit_handler)

icons = [demon, fantom_blue_md, fantom_blue_tl, fantom_red_tl,
         fantom_red_tr, skull, skull_front,
         skull_front_red, bender, ghost, green_ghost, pumpkin, creeper]

while True:
    try:
        sense.set_pixels(random.choice(icons))
        sleep(1)

    except KeyboardInterrupt:
        exit_handler(signal.SIGTERM)

exit_handler(signal.SIGTERM)
