"""
┌─────────────────────┐
│ Some math utilities │
└─────────────────────┘

 Florian Dupeyron
 July 2022
"""

import math

def sin(phase: float):
    phase -= math.floor(phase)
    return math.sin(2*math.pi*phase)/2+0.5

def range(phase: float, v_min: float = 0, v_max: float = 1):
    return phase*(v_max-v_min)+v_min
