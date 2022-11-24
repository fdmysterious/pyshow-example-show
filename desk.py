"""
┌───────────────┐
│ Command stuff │
└───────────────┘

 Florian Dupeyron
 August 2022
"""

from pyshow.osc.control import Control_Desk_OSC

osc_tablet = Control_Desk_OSC(host="0.0.0.0", port=5665)
