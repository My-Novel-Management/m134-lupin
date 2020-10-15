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
def nostalgic_friend(w: World):
    return w.scene('懐かしい友人',
            w.plot_note("帰りに昔よく通った駄菓子屋に立ち寄る"),
            w.plot_note("そこをやっていたおばあさんの姿はなく、同世代の女性がいた"),
            w.plot_note("小学校時代の同級生だった"),
            w.plot_note("話しかけられて懐かしいと言われるが、記憶が薄い"),
            w.plot_note("よく二人で秘密基地で遊んだと言われる"),
            w.plot_note("秘密基地を教わる"),
            )

