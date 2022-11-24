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
import os

import universe
from   transport import dmx_controller

# ──────────────── Control ─────────────── #

import desk

# ───────── import scenes groups ───────── #
import scenes.positions
import scenes.dimmer

import autoseqs.positions_fiesta

# ┌────────────────────────────────────────┐
# │ Event register utils                   │
# └────────────────────────────────────────┘

def register_autoseq(dk, loop, name, autoseq):
    dk.event_register(f"/{name}/enable", lambda x: autoseq.enable(loop, x))

def register_scene_choose(dk, page, name, chooser):
    dk.event_register(f"/{page}/{name}", lambda x: chooser.choose(name))


async def main():
    logging.basicConfig(level=logging.DEBUG if os.getenv("DEBUG") else logging.INFO)
    period = 0.01
    loop   = asyncio.get_running_loop()

    # ─────────── Register controls ────────── #

    register_autoseq     (desk.osc_tablet, loop, "autoseq_fiesta", autoseqs.positions_fiesta.autoseq)

    register_scene_choose(desk.osc_tablet, "positions"     , "up"               , scenes.positions.chooser)
    register_scene_choose(desk.osc_tablet, "positions"     , "down"             , scenes.positions.chooser)
    register_scene_choose(desk.osc_tablet, "positions"     , "face"             , scenes.positions.chooser)
    register_scene_choose(desk.osc_tablet, "positions"     , "star"             , scenes.positions.chooser)
    register_scene_choose(desk.osc_tablet, "positions"     , "circle_slow"      , scenes.positions.chooser)
    register_scene_choose(desk.osc_tablet, "positions"     , "circle_fast"      , scenes.positions.chooser)

    register_scene_choose(desk.osc_tablet, "dimmer"        , "on"               , scenes.dimmer.chooser   )
    register_scene_choose(desk.osc_tablet, "dimmer"        , "off"              , scenes.dimmer.chooser   )
    register_scene_choose(desk.osc_tablet, "dimmer"        , "on_fade"          , scenes.dimmer.chooser   )
    register_scene_choose(desk.osc_tablet, "dimmer"        , "off_fade"         , scenes.dimmer.chooser   )
    register_scene_choose(desk.osc_tablet, "dimmer"        , "chaser_left_slow" , scenes.dimmer.chooser   )


    
    # ─────────── Open start stuff ─────────── #

    dmx_controller.open()
    desk.osc_tablet.start(loop)

    last_exec = time.time()
    try:

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
