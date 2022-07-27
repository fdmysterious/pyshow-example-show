"""
┌────────────────────────┐
│ Controller declaration │
└────────────────────────┘

 Florian Dupeyron
 July 2022
"""

from pyshow.dmx.stm32dmx import DMX_Controller_STM32

dmx_controller = DMX_Controller_STM32("/dev/ttyACM0")
