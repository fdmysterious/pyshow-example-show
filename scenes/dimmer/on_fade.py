"""
┌───────────────────────────┐
│ Scene all on  with fading │
└───────────────────────────┘

 Florian Dupeyron
 July 2022
"""

from pyshow.core.scenes    import Scene
from pyshow.core.functions import Function_Fade

import universe

scene = Scene(
    functions = [
        Function_Fade(
            interface   = fixt.interfaces["dimmer"],
            target      = 100.0,
            fade_time_s = 5.0
        )
        for fixt in universe.all()
    ]
)
