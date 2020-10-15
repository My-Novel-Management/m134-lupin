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
def lost_clocktower(w: World):
    return w.scene('失われた時計塔',
            w.plot_note("急に戻ってきたので小言を言われる"),
            w.plot_note("$akiは両親に古い時計塔のことを尋ねる"),
            w.plot_note("時計塔なんてないと言われてしまう"),
            )

