"""
┌──────────────────────┐
│ Slow circle movement │
└──────────────────────┘

 Florian Dupeyron
 July 2022
"""

import math

from pyshow.core.functions import Function_Periodic_Expr
from pyshow.core.scenes    import Scene

from functools             import partial

from utils                 import m

import universe


__PERIOD       = 10  # s
__REFRESH_RATE = 0.2 # s

def rotfunc(fkt, t, dephase=0.0, v_min: float=0.0, v_max: float=1.0, invert=False):
    p = t/__PERIOD + dephase
    if invert:
        p = 1.0 - p

    return m.range(m.sin(p), v_min=v_min, v_max=v_max)

scene = Scene(functions = [
    # ─────────────── Pan wash ─────────────── #
    
    Function_Periodic_Expr(
        interface = universe.wash_L.interfaces["pos"].pan,
        period_s  = 0.2,
        expr      = partial(rotfunc, dephase=0.0, v_min=0.0, v_max=360.0, invert=False)
    ),

    Function_Periodic_Expr(
        interface = universe.wash_R.interfaces["pos"].pan,
        period_s  = 0.2,
        expr      = partial(rotfunc, dephase=0.0, v_min=0.0, v_max=360.0, invert=True)
    ),

    # ─────────────── Pan spots ────────────── #

    Function_Periodic_Expr(
        interface = universe.spot_L.interfaces["pos"].pan,
        period_s  = 0.2,
        expr      = partial(rotfunc, dephase=0.5, v_min=0.0, v_max=360.0, invert=False)
    ),

    Function_Periodic_Expr(
        interface = universe.spot_R.interfaces["pos"].pan,
        period_s  = 0.2,
        expr      = partial(rotfunc, dephase=0.5, v_min=0.0, v_max=360.0, invert=True)
    ),
    
])
