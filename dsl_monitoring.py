import os
import random
import signal
import sys
from time import sleep

import schedule
from colors import blue, cyan, indigo, orange, pink, purple, red, yellow
from icons import (demon, fantom_blue_md, fantom_blue_tl, fantom_red_tl,
                   fantom_red_tr, skull, skull_front,
                   skull_front_red, bender, ghost, green_ghost, pumpkin, creeper)
from sense_hat import SenseHat

sense = SenseHat()
sense.low_light = True
sense.set_rotation(270)

icons = [demon, fantom_blue_md, fantom_blue_tl, fantom_red_tl,
         fantom_red_tr, skull, skull_front,
         skull_front_red, bender, ghost, green_ghost, pumpkin, creeper]

def exit_handler(signal):
    sense.clear()
    sys.exit(0)


def ping():
    sense.clear()

    # Pick random color and line
    y = random.randrange(7)
    (R, G, B) = random.choice(
        [blue, cyan, indigo, orange, pink, purple, red, yellow])

    # Display ping start
    for i in range(8):
        sense.set_pixel(i, y, R, G, B)
        sleep(0.05)

    # Select a random DNS IP
    ping_ips = [
        "1.1.1.1",  # Cloudflare
        "8.8.8.8",  # Google DNS
        "8.8.4.4",  # Google DNS
    ]
    ping_ip = random.choice(ping_ips)

    # Ping DNS IP
    response = os.popen(f"ping {ping_ip} -c 1").read()

    # Display ping ended
    for i in range(8):
        sense.set_pixel(i, y, 0, 0, 0)
        sleep(0.05)

    if "1 packets transmitted, 1 received, 0% packet loss" in response:
        sense.clear()
    else:
        sense.clear()
        sense.set_pixels(random.choice(icons))


# Exit handling
signal.signal(signal.SIGTERM, exit_handler)

# Schedule jobs
schedule.every(15).seconds.do(ping)
ping()

while True:
    try:
        schedule.run_pending()
        sleep(1)
    except KeyboardInterrupt:
        exit_handler(signal.SIGTERM)
