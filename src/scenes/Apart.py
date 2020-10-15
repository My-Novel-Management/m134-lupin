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
def lupin_letter(w: World):
    return w.scene('$lupinからの手紙',
            w.plot_note("家に戻ってくる"),
            w.plot_note("手紙が届いていた"),
            w.plot_note("心あたりのない$full_lupinという人物からだったが"),
            w.plot_note("そこには「大切なものをもらった」と"),
            w.plot_note("返してほしかったら預けたものを渡せとあった"),
            w.plot_note("しかし全然心当たりがなかった"),
            )

