"""
┌───────────────┐
│ Scene all off │
└───────────────┘

 Florian Dupeyron
 July 2022
"""

from pyshow.core.scenes    import Scene
from pyshow.core.functions import Function_Static

import universe

scene = Scene(
    functions = [
        Function_Static(
            interface = universe.wash_L.interfaces["dimmer"],
            target    = 0.0
        ),

        Function_Static(
            interface = universe.wash_R.interfaces["dimmer"],
            target    = 0.0
        ),

        Function_Static(
            interface = universe.spot_L.interfaces["dimmer"],
            target    = 0.0
        ),

        Function_Static(
            interface = universe.spot_R.interfaces["dimmer"],
            target    = 0.0
        ),
    ]
)
