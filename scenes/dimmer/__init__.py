"""
┌───────────────┐
│ Dimmer scenes │
└───────────────┘

 Florian Dupeyron
 July 2022
"""

from pyshow.core.scenes import (
    Scene_Chooser
)

# ──────────── scenes import  ──────────── #

from .off      import scene as scene_off
from .on       import scene as scene_on

from .off_fade import scene as scene_off_fade
from .on_fade  import scene as scene_on_fade

from .chaser_left_slow import scene as scene_chaser_left_slow

# ───────────── chooser decl. ──────────── #

chooser = Scene_Chooser(scenes={
    "off":               scene_off,
    "on" :               scene_on,
    "off_fade":          scene_off_fade,
    "on_fade":           scene_on_fade,

    "chaser_left_slow":  scene_chaser_left_slow
    #"chaser_left_fast":  scene_chaser_left_fast,

    #"chaser_right_slow": scene_chaser_right_slow,
    #"chaser_right_fast": scene_chaser_right_fast,
})

