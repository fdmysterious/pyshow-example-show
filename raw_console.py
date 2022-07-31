"""
┌──────────────────────────────┐
│ Raw console to create scenes │
└──────────────────────────────┘

 Florian Dupeyron
 July 2022
"""

import os

import logging
import asyncio
import universe
from   transport import dmx_controller

from pyshow.osc.control import Control_Desk_OSC

ctrl = Control_Desk_OSC(host="0.0.0.0", port=5665)

def register_wash(fixture, page_name: str):
    ctrl.event_register(f"/{page_name}/mode-RGB",   lambda x: fixture.interfaces["mode"].set("rgb")  )
    ctrl.event_register(f"/{page_name}/mode-auto7", lambda x: fixture.interfaces["mode"].set("auto7"))
    ctrl.event_register(f"/{page_name}/mode-auto8", lambda x: fixture.interfaces["mode"].set("auto8"))
    ctrl.event_register(f"/{page_name}/mode-auto9", lambda x: fixture.interfaces["mode"].set("auto9"))

    ctrl.event_register(f"/{page_name}/R",lambda x: fixture.interfaces["color"].r.set(x))
    ctrl.event_register(f"/{page_name}/G",lambda x: fixture.interfaces["color"].g.set(x))
    ctrl.event_register(f"/{page_name}/B",lambda x: fixture.interfaces["color"].b.set(x))

    ctrl.event_register(f"/{page_name}/strobe",lambda x: fixture.interfaces["strobe"].set(x))
    ctrl.event_register(f"/{page_name}/dimmer",lambda x: fixture.interfaces["dimmer"].set(x))
    ctrl.event_register(f"/{page_name}/speed",lambda x: fixture.interfaces["speed"].set(x))

    ctrl.event_register(f"/{page_name}/pos",lambda x,y: fixture.interfaces["pos"].set(x,y))

def register_spot(fixture, page_name: str):
    ctrl.event_register(f"/{page_name}/color-white", lambda x: fixture.interfaces["color"].set("white"))
    ctrl.event_register(f"/{page_name}/color-magenta", lambda x: fixture.interfaces["color"].set("magenta"))
    ctrl.event_register(f"/{page_name}/color-green", lambda x: fixture.interfaces["color"].set("green"))
    ctrl.event_register(f"/{page_name}/color-blue", lambda x: fixture.interfaces["color"].set("blue"))
    ctrl.event_register(f"/{page_name}/color-yellow", lambda x: fixture.interfaces["color"].set("yellow"))
    ctrl.event_register(f"/{page_name}/color-orange", lambda x: fixture.interfaces["color"].set("orange"))
    ctrl.event_register(f"/{page_name}/color-cyan", lambda x: fixture.interfaces["color"].set("cyan"))
    ctrl.event_register(f"/{page_name}/color-purple", lambda x: fixture.interfaces["color"].set("purple"))
    ctrl.event_register(f"/{page_name}/color-purple_cyan", lambda x: fixture.interfaces["color"].set("purple_cyan"))
    ctrl.event_register(f"/{page_name}/color-cyan_orange", lambda x: fixture.interfaces["color"].set("cyan_orange"))
    ctrl.event_register(f"/{page_name}/color-orange_yellow", lambda x: fixture.interfaces["color"].set("orange_yellow"))
    ctrl.event_register(f"/{page_name}/color-yellow_blue", lambda x: fixture.interfaces["color"].set("yellow_blue"))
    ctrl.event_register(f"/{page_name}/color-blue_green", lambda x: fixture.interfaces["color"].set("blue_green"))
    ctrl.event_register(f"/{page_name}/color-green_magenta", lambda x: fixture.interfaces["color"].set("green_magenta"))

    ctrl.event_register(f"/{page_name}/gobo-plain", lambda x: fixture.interfaces["gobo"].set("plain"))
    ctrl.event_register(f"/{page_name}/gobo-circles", lambda x: fixture.interfaces["gobo"].set("circles"))
    ctrl.event_register(f"/{page_name}/gobo-alien", lambda x: fixture.interfaces["gobo"].set("alien"))
    ctrl.event_register(f"/{page_name}/gobo-fireworks", lambda x: fixture.interfaces["gobo"].set("fireworks"))
    ctrl.event_register(f"/{page_name}/gobo-rocks", lambda x: fixture.interfaces["gobo"].set("rocks"))
    ctrl.event_register(f"/{page_name}/gobo-bubbles", lambda x: fixture.interfaces["gobo"].set("bubbles"))
    ctrl.event_register(f"/{page_name}/gobo-vortex", lambda x: fixture.interfaces["gobo"].set("vortex"))
    ctrl.event_register(f"/{page_name}/gobo-zebra", lambda x: fixture.interfaces["gobo"].set("zebra"))

    ctrl.event_register(f"/{page_name}/strobe",lambda x: fixture.interfaces["strobe"].set(x))
    ctrl.event_register(f"/{page_name}/dimmer",lambda x: fixture.interfaces["dimmer"].set(x))
    ctrl.event_register(f"/{page_name}/speed",lambda x: fixture.interfaces["speed"].set(x))

    ctrl.event_register(f"/{page_name}/pos",lambda x,y: fixture.interfaces["pos"].set(x,y))

async def main():
    logging.basicConfig(level=logging.DEBUG if bool(os.getenv("DEBUG", False)) else logging.INFO)

    loop = asyncio.get_running_loop()
    register_wash(universe.wash_L, "wash_L")
    register_wash(universe.wash_L, "wash_R")
    register_spot(universe.spot_L, "spot_L")
    register_spot(universe.spot_R, "spot_R")

    dmx_controller.open()
    ctrl.start(loop)

    try:
        while True:
            await asyncio.sleep(5)
    finally:
        ctrl.stop()
        dmx_controller.close()

asyncio.run(main())
