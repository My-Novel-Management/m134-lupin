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
def my_treasure(w: World):
    return w.scene('私の宝物',
            w.plot_note("秘密基地は学校の裏山にあった"),
            w.plot_note("小さなお堂のそばの洞穴（防空壕後）に色々と持ち込んで作ったのだ"),
            w.plot_note("その時、もう一人、男の子がいたことを思い出す"),
            w.plot_note("そこに$lupinが現れた"),
            w.plot_note(""),
            )

