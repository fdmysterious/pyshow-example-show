"""
┌───────────────┐
│ Scene all on  │
└───────────────┘

 Florian Dupeyron
 July 2022
"""

from pyshow.core.scenes    import Scene
from pyshow.core.functions import Function_Static, Function_Animation_Expr

from functools             import partial

import universe

from utils import m

__PERIOD       = 1  # s

def dimfunc(fkt, t, dephase, invert):
    p = t/__PERIOD + dephase
    if invert:
        p = 1.0 - p

    return m.range(m.sin(p), 0.0, 100.0)

scene = Scene(
    functions = [
        Function_Animation_Expr(
            interface = universe.wash_L.interfaces["dimmer"],
            expr      = partial(dimfunc, dephase=0.0, invert=False)
        ),

        Function_Animation_Expr(
            interface = universe.wash_R.interfaces["dimmer"],
            expr      = partial(dimfunc, dephase=0.75, invert=False)
        ),

        Function_Animation_Expr(
            interface = universe.spot_L.interfaces["dimmer"],
            expr      = partial(dimfunc, dephase=0.25, invert=False)
        ),

        Function_Animation_Expr(
            interface = universe.spot_R.interfaces["dimmer"],
            expr      = partial(dimfunc, dephase=0.5, invert=False)
        ),
    ]
)
