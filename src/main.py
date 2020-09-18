#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
# from scenes import xxx


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8: 1K
#   4. Spec
#   5. Plot         - 1/4: 2K
#   6. Scenes
#   7. Conte        - 1/2: 4K
#   8. Layout
#   9. Draft        - 1/1: 8K
#
################################################################

# Constant
TITLE = "ミスタールパンの忘れ物"
MAJOR, MINOR, MICRO = 0, 1, 0
COPY = "ヒーローと怪盗は遅れてやってくる"
ONELINE = "約8000字の青春ミステリ短編。子どもの頃にある約束をした通称ルパンが、大人になった彼女の前に現れた"
OUTLINE = "約8000字の青春ミステリ短編。"
THEME = "子どもの頃の憧れ"
GENRE = "ミステリ／青春"
TARGET = "10-50years"
SIZE = "8K"
CONTEST_INFO = "妄想コンテスト「隠しごと」"
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
TAGS = ["ドラマ", "ミステリ", "青春"]
RELEASED = (10, 11, 2020)


# Episodes
def ch_main(w: World):
    return w.chapter('main',
            )


# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            )

def plot_note(w: World):
    return w.writer_note("プロットメモ",
            "会社でへとへとになって帰宅するとそこには見知らぬ男性がいた",
            "彼は「ルパン」だという",
            "それは幼い頃によく遊んでもらった近所のお兄さんで、手先が器用な人だった",
            "彼が忘れ物を取りに来たというのだが、それを彼女は持っていない",
            "彼は思い出せるようにとあるものを預けて立ち去る",
            "忘れた頃に彼は再びやってきて、今度は別のものを預けてきた",
            "ある日、テレビで自分が持っているものが盗難品だと分かる",
            "警察に届けようか迷っていたところで、思い出した",
            "彼がある鍵を預けていたことを",
            "実家に戻り、古い時計塔に入る",
            "時計塔の一番てっぺんには動かなくなった目覚まし時計が飾られていた",
            "実は盗まれたものは、そこから盗み出されたものだったのだ",
            "彼はそこにやってくる",
            "ルパンと対峙する",
            "ルパンは真実を語り始めた",
            "からくり時計は今、成功者となっている男が盗み出したものだった",
            "彼は犯罪を犯した。",
            )

def chara_note(w: World):
    return w.writer_note("人物メモ",
            "・大人になってしまった子ども（女性）",
            "会社員とかで働きながら疲れてはくたばる毎日",
            "部屋に戻ると、鍵があいていた。完全に泥棒と思ったら面影があり思い出す。ルパンさん",
            "・忘れ物を取りに来たルパン（男性）",
            "一番のキーポイント。実在するかすら怪しい。最後までそれでいくかな",
            "あとは家族とか、友人とかか",
            )

def stage_note(w: World):
    return w.writer_note("舞台メモ",
            )

def theme_note(w: World):
    return w.writer_note("テーマメモ",
            "子どもの頃の無駄に無茶なことや悪そうなことをかっこいいと憧れた、その無垢な気持ち",
            "大人になるとある程度子どもの頃の気持ちが薄れてしまう",
            )

def motif_note(w: World):
    return w.writer_note("モチーフ",
            # main
            "怪盗", "盗む", "隠す", "宝物", "忘れ物",
            "子ども時代",
            # sub
            "青春時代", "子ども時代",
            "夢",
            "ミステリ",
            )


# Main
def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_taginfos(*TAGS)
    w.config.set_released(*RELEASED)
    return w.run(
            writer_note(w),
            plot_note(w),
            chara_note(w),
            stage_note(w),
            theme_note(w),
            motif_note(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

