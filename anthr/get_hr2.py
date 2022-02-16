
from ant.easy.node import Node
from ant.easy.channel import Channel
from ant.base.message import Message

import logging
from datetime import datetime
from threading import Lock
import os
import time


NETWORK_KEY = [0xB9, 0xA5, 0x21, 0xFB, 0xBD, 0x72, 0xC3, 0x45]

class HeartRate(object):
    def __init__(self,filename=None,  output_path="."):
        self.heart_rate = None
        self.lock = Lock() 
        self._start_time = None

        #Set the filename
        if filename is None:
            filename = datetime.now().strftime("%Y_%m_d_%H_%M_%S") + ".csv"
        
        self.filename = filename

        # Set the filepath
        self.output_path = output_path

        self.output_filename = os.path.join(output_path, filename)
        print("--------------------------------")
        print(f"Output File: {self.output_filename}")
        print(f'Starting Time: {datetime.now().strftime("%Y-%m-d %H:%M:%S")}')

        with open(self.output_filename, "w") as f:
            f.write("posix_timestamp,heart_rate\n")
    

    def on_data(self,data):
        
        with self.lock:

            if self._start_time is None:
                self._start_time = time.time()
            
            self.heartrate = data[7]

            with open(self.output_filename, "a") as f:
                f.write(f"{time.time()},{self.heartrate}\n")

        elapsed_time = time.time() - self._start_time 
        print(f"Elapsed Time (s): {elapsed_time:.2f}", end="\r")




def get_hr(filename=None, output_path='.'):
    # logging.basicConfig()

    node = Node()
    node.set_network_key(0x00, NETWORK_KEY)

    channel = node.new_channel(Channel.Type.BIDIRECTIONAL_RECEIVE)

    hr = HeartRate(filename=filename, output_path=output_path)

    channel.on_broadcast_data = hr.on_data
    channel.on_burst_data = hr.on_data

    channel.set_period(8070)
    channel.set_search_timeout(12)
    channel.set_rf_freq(57)
    channel.set_id(0, 120, 0)

    try:
        channel.open()
        node.start()
    finally:
        node.stop()

