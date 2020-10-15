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
def back_home(w: World):
    return w.scene('地元への帰省',
            w.plot_note("地元の田舎町の最寄り駅に戻ってくる"),
            w.plot_note("東京とは違い、何もない"),
            w.plot_note("寂れた街並み"),
            w.plot_note("バスは来ないから、仕方なく徒歩で実家に向かう"),
            )

