"""親クラス
block,player,enemy,foodの親クラス
"""


class Item:
    """block,player,enemy,foodの親クラス

    Attributes:
       now_x(int) : 現在のx座標
       now_y(int) : 現在のy座標
       status(bool) : アイテムの状態（Trueなら存在する、Falseなら存在しない消滅した）
       icon(str) : 表示されるアイテムのアイコン

    Examples:
        >>> item = Item(3, 3)
        >>> item.now_x
        3
        >>> item.now_y
        3
        >>> item.icon
        ''
        >>> item.status
        True
    """

    def __init__(self, x, y) -> None:
        self.now_x = x
        self.now_y = y
        self.status = True
        self.icon = ""
