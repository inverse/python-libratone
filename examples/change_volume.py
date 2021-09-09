#!/usr/bin/python
import logging
import sys

from libratone.client import send_command
from libratone.commands import get_volume

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("You must provide <ip-address> <volume-level>")
        exit(1)

    logging.basicConfig(level=logging.DEBUG)

    ip_address = sys.argv[1]
    volume_level = int(sys.argv[2])
    send_command(ip_address, get_volume(volume_level))
