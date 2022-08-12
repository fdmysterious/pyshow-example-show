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
            target    = 180.0
        ),

        Function_Static(
            interface = universe.wash_L.interfaces["pos"].tilt,
            target    = 180.0
        ), 


        Function_Static(
            interface = universe.wash_R.interfaces["pos"].pan,
            target    = 180.0
        ),

        Function_Static(
            interface = universe.wash_R.interfaces["pos"].tilt,
            target    = 180.0
        ), 


        Function_Static(
            interface = universe.spot_L.interfaces["pos"].pan,
            target    = 180.0
        ),

        Function_Static(
            interface = universe.spot_L.interfaces["pos"].tilt,
            target    = 180.0
        ), 
        

        Function_Static(
            interface = universe.spot_R.interfaces["pos"].pan,
            target    = 180.0
        ),

        Function_Static(
            interface = universe.spot_R.interfaces["pos"].tilt,
            target    = 180.0
        ), 
    ]
)
