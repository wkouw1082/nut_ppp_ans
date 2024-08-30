from item import Item
import doctest


class Block(Item):
    """
    Blockクラス
    アイテムの位置とアイコンを管理するクラス

    Attributes:
        x (int): x座標
        y (int): y座標
        icon (str): 表示アイコン

    Examples:
        >>> block = Block(3, 3)
        >>> block.now_x
        3
        >>> block.now_y
        3
        >>> block.icon
        '#'
        >>> isinstance(block, Item)
        True
    """

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.icon = "#"


if __name__ == "__main__":
    doctest.testmod()
