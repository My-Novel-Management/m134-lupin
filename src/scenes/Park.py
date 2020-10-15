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
def nothing_tower(w: World):
    return w.scene('塔なんてなかった',
            w.plot_note("自分のおぼろげな記憶を頼りにその場所にいってみる"),
            w.plot_note("新しく整備された公園で、時計塔なんてなかった"),
            w.plot_note("そこで遊んでいた母子に尋ねてもこの辺りはずっと野原だったと"),
            )

