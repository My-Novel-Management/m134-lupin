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
def couple_talk(w: World):
    return w.scene('恋人の会話',
            w.plot_note("映画を見終わり、その感想を語り合う"),
            w.plot_note("けれど$akiはそれよりずっと気がかりなことがあった"),
            w.plot_note("彼から貰ったはずのペアリングがどこかにいってしまって、言い出せない"),
            w.plot_note("彼への隠し事があったのだ"),
            )

