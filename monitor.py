#!/usr/bin/env python3

import os
import signal
import sys
from time import sleep

from icons import (fantom_red_tl, fantom_red_tr, pink_heart,
                   pink_heart_crossed, red_heart, red_heart_crossed,
                   red_heart_empty_crossed)
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(270)


def exit_handler(signal):
    sense.clear()
    sys.exit(0)


signal.signal(signal.SIGTERM, exit_handler)

while True:
    try:
        sense.set_pixels(pink_heart)
        sleep(1)
        sense.set_pixels(pink_heart_crossed)
        sleep(1)

        sense.set_pixels(red_heart)
        sleep(1)
        sense.set_pixels(red_heart_crossed)
        sleep(1)

        sense.set_pixels(fantom_red_tl)
        sleep(1)
        sense.set_pixels(fantom_red_tr)
        sleep(1)

    except KeyboardInterrupt:
        exit_handler(signal.SIGTERM)

exit_handler(signal.SIGTERM)
