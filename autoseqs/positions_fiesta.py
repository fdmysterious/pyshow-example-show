"""
┌────────────────────────────────────┐
│ Autoseq for positions fiesta mode! │
└────────────────────────────────────┘

 Florian Dupeyron
 August 2022
"""


from pyshow.core.control import Auto_Sequencer
from scenes.positions    import chooser as pos_chooser

autoseq = Auto_Sequencer( steps=[
    (10, 20, lambda: pos_chooser.choose("circle_slow")),
    (10, 20, lambda: pos_chooser.choose("circle_fast")),
    (10, 20, lambda: pos_chooser.choose("up"         )),
    (10, 20, lambda: pos_chooser.choose("face"       )),
    (10, 20, lambda: pos_chooser.choose("star"       ))
], randomize=True)
