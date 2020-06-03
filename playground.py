#!/usr/bin/env python3

import os
import signal
import sys
from time import sleep

from icons import (demon, fantom_blue_md, fantom_blue_tl, fantom_red_tl,
                   fantom_red_tr, pink_heart, red_heart, skull, skull_front,
                   skull_front_red)
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(270)


def exit_handler(signal):
    sense.clear()
    sys.exit(0)


signal.signal(signal.SIGTERM, exit_handler)

while True:
    try:
        for img in [demon, fantom_red_tl, fantom_red_tr, fantom_blue_tl,
                    fantom_blue_md, pink_heart, red_heart,
                    skull, skull_front, skull_front_red]:
            sense.set_pixels(img)
            sleep(0.8)

    except KeyboardInterrupt:
        exit_handler(signal.SIGTERM)

exit_handler(signal.SIGTERM)
