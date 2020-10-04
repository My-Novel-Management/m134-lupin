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
            "ミスタールパンからのメッセージが届く",
            "彼氏がいる",
            "$akiは彼氏に隠し事をしているっぽい",
            "家の中での服装はずぼらだし、化粧もほぼしない",
            "パズルや骨組みが好き",
            "プラモデルをスケルトンにして悦に入っている",
            "そんな過去をもっていたが、段ボール箱に捨てた",
            "ミスタールパンは小さい頃に出会った",
            "ミスタールパンが預けた忘れ物を取りに来ると予告",
            "思い出せないまま",
            "彼氏に普段着がばれる",
            "彼氏にミスタールパンがばれる",
            "",
            # TODO
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
            "記憶を巡るミステリ、にするか、世界系のミステリにするか",
            "クラリス症候群、という名前を使う",
            "自分を塔から助け出してくれる泥棒さんに憧れを抱く",
            # TODO: 隠し事のキーポイント、展開、オチを見つける
            "時計塔に隠されていたのは「子どもの頃の情熱」だった",
            "ファンタジックなオチでいくかな",
            "子どもの情熱を示す「おもちゃ」って何だろう。玩具じゃなくてもいい",
            "今でこそ「女らしさ」をまとっているけれど、心の中にはメカオタクの血を騒がせている",
            "彼氏からもそんなことを言われるけれど、そうじゃないんだ。自分の本来は",
            "自分を取り戻す物語",
            "表面上は「彼への隠しごと」として読み進める",
            "それはルパンというコードネームの「彼氏」と思わせておく",
            "でも違っていた",
            "ミスタールパンは「過去の自分」だ",
            "それとずっとやりとりしていた",
            )

def chara_note(w: World):
    return w.writer_note("人物メモ",
            "・大人になってしまった子ども（女性）",
            "会社員とかで働きながら疲れてはくたばる毎日",
            "部屋に戻ると、鍵があいていた。完全に泥棒と思ったら面影があり思い出す。ルパンさん",
            "昔は陸上部だったとか。走ることで憂さ晴らしをしていた。それが青春だった",
            "でも今は「情熱」はない",
            "・忘れ物を取りに来たルパン（男性）",
            "一番のキーポイント。実在するかすら怪しい。最後までそれでいくかな",
            "あとは家族とか、友人とかか",
            "＊彼氏：現在付き合っている男性。色々と細かいところを気にする。$akiに女性らしさを求めてくる",
            )

def stage_note(w: World):
    return w.writer_note("舞台メモ",
            "田舎と都会の対比もしたい",
            "現在は都会の雑踏の中で毎日の忙しさに紛れている",
            "機械とか便利なものによって「考えること」から離れてしまっている",
            "でも子供時代は「考えてばかり」だった",
            "その象徴としての「時計塔」があった",
            )

def theme_note(w: World):
    return w.writer_note("テーマメモ",
            "子どもの頃の無駄に無茶なことや悪そうなことをかっこいいと憧れた、その無垢な気持ち",
            "大人になるとある程度子どもの頃の気持ちが薄れてしまう",
            "がむしゃらな情熱。わがままと呼ばれても突っ切っていくような熱量",
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
            "クラリス症候群",
            "シンデレラ",
            "自分では何もしない",
            "待っているだけ",
            "時計", "時間",
            "戻らないもの",
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

