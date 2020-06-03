import os
import random
import signal
import sys
from time import sleep

import schedule
from colors import blue, cyan, indigo, orange, pink, purple, red, yellow
from icons import pink_heart, skull_front
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(270)


def exit_handler(signal):
    sense.clear()
    sys.exit(0)


def ping():
    # Display ping in progress
    y = random.randrange(7)
    for i in range(8):
        (R, G, B) = random.choice(
            [blue, cyan, indigo, orange, pink, purple, red, yellow])
        sense.set_pixel(i, y, R, G, B)
        sleep(0.05)
    for i in range(8):
        sense.set_pixel(i, y, 0, 0, 0)
        sleep(0.05)

    # Select a random DNS IP
    ping_ips = [
        "1.1.1.1",  # Cloudflare
        "8.8.8.8",  # Google DNS
        "8.8.4.4",  # Google DNS
    ]
    ping_ip = random.choice(ping_ips)

    response = os.popen(f"ping {ping_ip} -c 1").read()
    if "1 packets transmitted, 1 received, 0% packet loss" in response:
        sense.clear()
    else:
        sense.clear()
        sense.set_pixels(skull_front)


# Exit handling
signal.signal(signal.SIGTERM, exit_handler)

# Schedule jobs
schedule.every(15).seconds.do(ping)

while True:
    try:
        schedule.run_pending()
        sleep(1)
    except KeyboardInterrupt:
        exit_handler(signal.SIGTERM)
