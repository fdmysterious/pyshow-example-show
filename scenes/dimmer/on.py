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
            interface = fixt.interfaces["dimmer"],
            target    = 100.0
        )
        for fixt in universe.all()
    ]
)
