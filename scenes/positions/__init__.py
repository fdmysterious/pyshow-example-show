"""
┌──────────────────┐
│ Positions scenes │
└──────────────────┘

 Florian Dupeyron
 July 2022
"""

from pyshow.core.scenes import (
    Scene_Chooser
)

# ───────────── scenes import ──────────── #

from .up   import scene as scene_up
from .down import scene as scene_down
from .star import scene as scene_star
from .face import scene as scene_face

from .circle_slow import scene as scene_circle_slow
from .circle_fast import scene as scene_circle_fast

chooser = Scene_Chooser(scenes={
    "up"  : scene_up,
    "down": scene_down,
    "star": scene_star,
    "face": scene_face,

    "circle_slow": scene_circle_slow,
    "circle_fast": scene_circle_fast
})
