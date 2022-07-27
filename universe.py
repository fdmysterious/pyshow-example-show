"""
┌──────────────────────┐
│ Universe declaration │
└──────────────────────┘

 Florian Dupeyron
 July 2022
"""

from pyshow.core.fixtures                    import Fixture

from pyshow.fixtures.nobrand.moving_head_60w import NoBrand_60W_MovingHead_11Ch
from pyshow.fixtures.starway.maxkolor18      import Starway_Maxkolor18_11Ch

from transport import dmx_controller


# ┌────────────────────────────────────────┐
# │ Fixtures instanciation                 │
# └────────────────────────────────────────┘

# ───────────────── Wash ───────────────── #

wash_L = Starway_Maxkolor18_11Ch    (transport=dmx_controller, channel_start=0 )
wash_R = Starway_Maxkolor18_11Ch    (transport=dmx_controller, channel_start=11)


# ───────────────── Spot ───────────────── #

spot_L = NoBrand_60W_MovingHead_11Ch(transport=dmx_controller, channel_start=22)
spot_R = NoBrand_60W_MovingHead_11Ch(transport=dmx_controller, channel_start=33)

def all():
    for x in locals():
        if isinstance(x, Fixture):
            yield x
