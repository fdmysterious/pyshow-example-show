"""
┌───────────────┐
│ Scene all on  │
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
            interface = universe.wash_L.interfaces["color"].r,
            target    = 1.0
        ),
        Function_Static(
            interface = universe.wash_L.interfaces["color"].g,
            target    = 1.0
        ),
        Function_Static(
            interface = universe.wash_L.interfaces["color"].b,
            target    = 1.0
        ),



        Function_Static(
            interface = universe.wash_R.interfaces["color"].r,
            target    = 1.0
        ),
        Function_Static(
            interface = universe.wash_R.interfaces["color"].g,
            target    = 1.0
        ),
        Function_Static(
            interface = universe.wash_R.interfaces["color"].b,
            target    = 1.0
        ),




        Function_Static(
            interface = universe.spot_R.interfaces["color"],
            target    = "white"
        ),

        Function_Static(
            interface = universe.spot_L.interfaces["color"],
            target    = "white"
        )
    ]
)
