from item import Item


class Player(Item):
    """プレイヤークラス
    Itemを継承して作成したプレイヤークラス.
    入力から移動方向を受け取って移動しようとする方向を計算するメソッドと
    マップから移動して良いと許可が出た時に呼び出される座標を更新するメソッド
    を追加.

    Attributes:
       新しい属性なし

    """

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.icon = "P"

    def move_next(self, key: tuple[int, int]) -> tuple[int, int]:
        """
        入力から移動方向を受け取って移動しようとする方向を計算するメソッド
        引数にキー入力から受け取った次に移動したい方向をとり,現在のプレイヤーの座標から次に移動したい座標を戻り値として出力する.

        Args:
            key (tuple[int, int]): キー入力から受け取った次に移動したい方向.(例:右に1マス移動したかったら(1,0)を受け取る)

        Returns:
            tuple[int, int]: 次に移動したい座標(例:入力が(1,0)で現在のプレイヤーの座標が(2,3)だった時,戻り値は(3,3))

        Examples:
            >>> player = Player(2, 3)
            >>> player.move_next((1, 0))
            (3, 3)

        """
        next_coordinate = (self.now_x + key[0], self.now_y + key[1])
        return next_coordinate

    def update_coordinate(self, next_coordinate: tuple[int, int]) -> None:
        """
        座標を更新するメソッド
        引数に次に移動したい座標をとり,その座標にプレイヤーの現在座標を更新する.

        Args:
            next_coordinate (tuple[int, int]): 次に移動したい座標

        Returns:
            None

        Examples:
            >>> player = Player(2, 3)
            >>> player.update_coordinate((3, 3))
            >>> player.now_x
            3
            >>> player.now_y
            3

        """
        self.now_x = next_coordinate[0]
        self.now_y = next_coordinate[1]
