# -*- coding: utf-8 -*-
'''
Stage: "stage name"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def couple_date(w: World):
    return w.scene('恋人とのデート',
            w.plot_note("MI最新作を見ている"),
            w.plot_note("彼氏は楽しみにしているが、$akiはあまり楽しくない"),
            w.plot_note(""),
            )

