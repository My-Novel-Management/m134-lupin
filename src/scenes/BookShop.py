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
def working(w: World):
    return w.scene('$akiの仕事',
            w.plot_note("$akiは本屋に勤めていた"),
            w.plot_note("書店員としての仕事をしながら、考え込む"),
            w.plot_note("店にやってきた老婦人は何か忘れたようだった"),
            w.plot_note("$akiも最近よく記憶が抜け落ちる"),
            w.plot_note("昔のことがあまり思い出せなかった"),
            )

