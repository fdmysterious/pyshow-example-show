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

chooser = Scene_Chooser(scenes={
    "up"  : scene_up,
    "down": scene_down
})
