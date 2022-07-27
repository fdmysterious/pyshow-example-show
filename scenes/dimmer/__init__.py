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

# ───────────── chooser decl. ──────────── #

chooser = Scene_Chooser(scenes={
    "off":      scene_off,
    "on" :      scene_on,
    "off_fade": scene_off_fade,
    "on_fade":  scene_on_fade
})

