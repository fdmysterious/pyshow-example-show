"""
┌───────────────────────────┐
│ Scene all off with fading │
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
            interface   = universe.wash_L.interfaces["dimmer"],
            target      = 0.0,
            fade_time_s = 5.0
        ),

        Function_Fade(
            interface   = universe.wash_R.interfaces["dimmer"],
            target      = 0.0,
            fade_time_s = 5.0
        ),

        Function_Fade(
            interface   = universe.spot_L.interfaces["dimmer"],
            target      = 0.0,
            fade_time_s = 5.0
        ),

        Function_Fade(
            interface   = universe.spot_R.interfaces["dimmer"],
            target      = 0.0,
            fade_time_s = 5.0
        ),
    ]
)
