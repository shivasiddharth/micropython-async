# htu_test.py Demo program for portable asynchronous HTU21D driver

import uasyncio as asyncio
from machine import Pin, I2C
import htu21d_mc

# Specify pullup: on my ESP32 board pullup resistors are not fitted :-(
scl_pin = Pin(22, pull=Pin.PULL_UP, mode=Pin.OPEN_DRAIN)
sda_pin = Pin(23, pull=Pin.PULL_UP, mode=Pin.OPEN_DRAIN)
# Standard port
i2c = I2C(-1, scl=scl_pin, sda=sda_pin)

# Loboris port (soon this special treatment won't be needed).
# https://forum.micropython.org/viewtopic.php?f=18&t=3553&start=390
#i2c = I2C(scl=scl_pin, sda=sda_pin)

htu = htu21d_mc.HTU21D(i2c, read_delay=2)

async def main():
    await htu
    while True:
        fstr = 'Temp {:5.1f} Humidity {:5.1f}'
        print(fstr.format(htu.temperature, htu.humidity))
        await asyncio.sleep(5)

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
