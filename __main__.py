"""
┌─────────────────────────────┐
│ Main file for mariage show! │
└─────────────────────────────┘

 Florian Dupeyron
 July 2022
"""

import asyncio
import logging
import time

import universe
from   transport import dmx_controller

# ───────── import scenes groups ───────── #
import scenes.positions
import scenes.dimmer

async def main():
    period = 0.01
    loop   = asyncio.get_running_loop()

    dmx_controller.open()

    last_exec = time.time()
    try:
        scenes.positions.chooser.choose("circle_slow")
        while True:
            tstamp = time.time()


            # Update stuff
            await scenes.positions.chooser.update(tstamp)
            await scenes.dimmer.chooser.update(tstamp)

            # Flush to controller
            dmx_controller.flush()

            # Sleep
            curtime   = time.time()
            await asyncio.sleep(curtime-last_exec+period)
            last_exec = time.time()

    except KeyboardInterrupt:
        pass
    finally:
        dmx_controller.close()

asyncio.run(main())
