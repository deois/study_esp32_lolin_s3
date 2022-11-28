import time

import machine

machine.freq()  # get the current frequency of the CPU
machine.freq(240000000)  # set the CPU frequency to 240 MHz

from machine import Pin
from neopixel import NeoPixel

neo = NeoPixel(Pin(38, Pin.OUT), 1)
neo.ORDER = (0, 1, 2, 3)
RGB = [100, 0, 0]
# pinLED = Pin(38, Pin.OUT)  # create output pin on GPIO0

def gradation():

    while True:
        for r in (0,257):
            RGB = [r, 0, 0]
            neo[0] = tuple(RGB)
            neo.write()
            print(RGB)
            time.sleep(0.05)
            for g in (0,257):
                RGB = [r, g, 0]
                neo[0] = tuple(RGB)
                neo.write()
                print(RGB)
                time.sleep(0.05)
                for b in (0,257):
                    RGB = [r, g, b]
                    neo[0] = tuple(RGB)
                    neo.write()
                    print(RGB)
                    time.sleep(0.05)
                    for b in (257, 0, -1):
                        RGB = [r, g, b]
                        neo[0] = tuple(RGB)
                        neo.write()
                        print(RGB)
                        time.sleep(0.05)
                        for g in (257, 0, -1):
                            RGB = [r, g, b]
                            neo[0] = tuple(RGB)
                            neo.write()
                            print(RGB)
                            time.sleep(0.05)
                            for r in (257, 0, -1):
                                RGB = [r, g, b]
                                neo[0] = tuple(RGB)
                                neo.write()
                                print(RGB)
                                time.sleep(0.05)

import network

# wlan = network.WLAN(network.STA_IF) # create station interface
# wlan.active(True)       # activate the interface
# wlan.scan()             # scan for access points
# wlan.isconnected()      # check if the station is connected to an AP
# wlan.connect('ssid', 'key') # connect to an AP
# wlan.config('mac')      # get the interface's MAC address
# wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses

# ap = network.WLAN(network.AP_IF) # create access-point interface
# ap.config(ssid='ESP-AP') # set the SSID of the access point
# ap.config(max_clients=10) # set how many clients can connect to the network
# ap.active(True)         # activate the interface

if __name__ == '__main__':
    gradation()