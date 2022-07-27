"""
┌──────────────┐
│ Scene all up │
└──────────────┘

 Florian Dupeyron
 July 2022
"""

from pyshow.core.scenes    import Scene
from pyshow.core.functions import Function_Static

import universe

scene = Scene(
    functions = [
        Function_Static(
            interface = universe.wash_L.interfaces["pos"].pan,
            target    = 202.5
        ),

        Function_Static(
            interface = universe.wash_L.interface["pos"].tilt,
            target    = 180.0-45
        ), 


        Function_Static(
            interface = universe.wash_R.interfaces["pos"].pan,
            target    = 337.5
        ),

        Function_Static(
            interface = universe.wash_R.interface["pos"].tilt,
            target    = 180.0.0-45
        ), 


        Function_Static(
            interface = universe.spot_L.interfaces["pos"].pan,
            target    = 247.5
        ),

        Function_Static(
            interface = universe.spot_L.interface["pos"].tilt,
            target    = 180.0-45
        ), 
        

        Function_Static(
            interface = universe.spot_R.interfaces["pos"].pan,
            target    = 292.5
        ),

        Function_Static(
            interface = universe.spot_R.interface["pos"].tilt,
            target    = 180.0-45
        ), 
    ]
)
