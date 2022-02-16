#!/usr/bin/env python

import os
import time
from datetime import datetime


from ant.core import driver
from ant.core.node import Node, Network, ChannelID
from ant.core.constants import NETWORK_KEY_ANT_PLUS, NETWORK_NUMBER_PUBLIC
from ant.plus.heartrate import HeartRate

import logging

from .defaults import SERIAL, LOG

logger = logging.getLogger(__name__)


def get_hr(filename=None, serial=SERIAL, output_path="."):
    """get the heartrate from the ant+ sensor and write to a file

    Args:
        filename (_type_, optional): the filename. Defaults to None.
        serial (_type_, optional): serial interface. Defaults to /dev/ttyUSB0.
        output_path (str, optional): ouptut path of resulting file. Defaults to ".".
    """
    device = driver.USB1Driver(serial, log=LOG)
    antnode = Node(device)
    antnode.start()
    network = Network(key=NETWORK_KEY_ANT_PLUS, name="N:ANT+")
    antnode.setNetworkKey(NETWORK_NUMBER_PUBLIC, network)

    hr = HeartRate(antnode, network)

    hr.open()

    if filename is None:
        filename = datetime.now().strftime("%Y_%m_d_%H_%M_%s") + ".csv"

    output_filename = os.path.join(output_path, filename)
    print("--------------------------------")
    print(f"Output File: {output_filename}")
    print(f"Serial Device: {serial}")
    print(f'Starting Time: {datetime.now().strftime("%Y-%m-d %H:%M:%s")}')

    starting_time = time.time()

    with open(output_filename, "w") as f:
        f.write("posix_timestamp,heart_rate\n")
        try:
            while True:
                elapsed_time = time.time() - starting_time
                print(f"Elapsed Time (s): {elapsed_time:.2f}", end="\r")
                f.write(f"{time.time()},{hr.computed_heart_rate}\n")
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("---COMPLETE---")
