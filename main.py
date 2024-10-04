# coding: utf-8

import random
from tkinterControl import Tkc

COLOR_DICT = {
    "b": "black",
    "r": "red",
    "g": "green",
    "c": "cyan",
    "p": "purple",
    # "h": "hotpink",
    # "l": "lime",
}
USE_STR = "A234567890JQK"

USE_CARD_COUNT = 13*7
MAX_COLUMN = 13*2

# ========================================

CARD_DATA = [
    m+n if n != "0" else m +
    "10" for m in COLOR_DICT.keys() for n in USE_STR
]
USE_CARD_COUNT = min(USE_CARD_COUNT, len(CARD_DATA))
MAX_COLUMN = min(MAX_COLUMN, USE_CARD_COUNT)


class g:
    nowOpen = 0
    oldCard = -1
    openCou = 0
    playTurn = 0


def main() -> None:
    def openCard(ind: int) -> None:
        if tkc.var.getValue(f"card_{ind}") != "":
            return
        if g.nowOpen >= 2:
            g.nowOpen = 0
            return
        g.nowOpen += 1
        cd = card[ind]
        tkc.var.updateValue(f"card_{ind}", cd[1:])
        if g.oldCard == -1:
            g.oldCard = ind
            return
        g.playTurn += 1
        if cd == card[g.oldCard]:
            tkc.wid.getWidget(f"card_{ind}").configure(
                bg="yellow",
            )
            tkc.wid.getWidget(f"card_{g.oldCard}").configure(
                bg="yellow",
            )
            g.openCou += 1
            if g.openCou >= USE_CARD_COUNT:
                if g.playTurn <= USE_CARD_COUNT:
                    tkc.messagebox.show(
                        "info",
                        "全てのカードを開いた！\n\nまさかまさかのノーミスクリア！！！",
                        "真剣衰弱",
                    )
                else:
                    tkc.messagebox.show(
                        "info",
                        f"全てのカードを開いた！\n\n{g.playTurn}ターンでクリア！！！",
                        "真剣衰弱",
                    )
                tkc.drawEnd()
            g.nowOpen = 0
            g.oldCard = -1
            return

        def res():
            tkc.var.updateValue(f"card_{ind}", "")
            tkc.var.updateValue(f"card_{g.oldCard}", "")
            g.nowOpen = 0
            g.oldCard = -1
        tkc.after(700, res)
    # 本体
    tkc = Tkc(
        title="神経(真剣)衰弱",
        windowSize=(MAX_COLUMN*45, int(USE_CARD_COUNT*2/MAX_COLUMN+0.99)*98),
        windowPos=(0, 0),
        resizable=(False, False)
    )
    tkc.createFont("card", "メイリオ", 8, "bold")
    card = CARD_DATA[:USE_CARD_COUNT]*2
    random.shuffle(card)
    for i, v in enumerate(card):
        x = i % MAX_COLUMN
        y = i // MAX_COLUMN
        tkc.wid.addButton(
            "",
            name=f"card_{i}",
            column=x, row=y,
            width=5, height=5,
            fg=COLOR_DICT[v[0]],
            font="card",
            takefocus=False,
            com=lambda e=None, i=i: openCard(i),
        )
    tkc.drawStart()


if __name__ == "__main__":
    main()
