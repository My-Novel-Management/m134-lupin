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
            w.plot_note("$lupinは昔ある男の子がいたことを語る"),
            )



def old_talk(w: World):
    return w.scene("昔話",
            w.plot_note("一人の男の子がいた"),
            w.plot_note("身体が弱く、よく本ばかり読んでいる子だった"),
            w.plot_note("そんな彼と友だちになった$akiは、彼のために秘密基地を作った"),
            w.plot_note("彼は$akiに怪盗ルパンの話を楽しそうに聞かせてくれた"),
            w.plot_note("それから彼は病気で入院してあえなくなった"),
            )


def lost_property(w: World):
    return w.scene("忘れ物",
            w.plot_note("$akiは思い出した"),
            w.plot_note("悲しい思い出としてずっと自分の中に封じ込めて隠していたもの"),
            w.plot_note("$lupinはあの時の男の子のあだ名だった"),
            w.plot_note("$akiはあの時の気持ちを打ち明ける"),
            w.plot_note("本当の自分の姿を封じて生きている今の息苦しさは、それが原因だった"),
            w.plot_note("その児童書を手にして、隠れ家を後にする"),
            )
