from item import Item
import random
import doctest


class Enemy(Item):
    """エネミークラス
    Itemを継承して作成したエネミークラス.
    ランダムに動きたい方向を計算する関数。（数字ごとに動く方向を当てはめて乱数で数字を与える。）と
    マップから移動して良いと許可が出たら座標を更新するメソッド
    を追加.

    Attributes:
       新しい属性なし

    """

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.icon = "E"

    def move_random(self) -> tuple[int, int]:
        """ランダムに動きたい方向を計算するメソッド.
        random.choice()を用いて上下左右のいずれかの方向を選択し、現在座標に加えて次に移動したい座標を計算する.

        Returns:
          tuple[int, int]: 移動したい座標

        Examples:
          >>> enemy = Enemy(2, 3)
          >>> possible_moves = [(3, 3), (1, 3), (2, 4), (2, 2)]
          >>> next_move = enemy.move_random()
          >>> next_move in possible_moves
          True

        """
        # 上下左右の方向を表す座標のリスト
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # ランダムに方向を選択して次に移動したい座標を計算
        next_direction = random.choice(directions)
        next_x = self.now_x + next_direction[0]
        next_y = self.now_y + next_direction[1]
        return (next_x, next_y)

    def update_coordinate(self, next_coordinate: tuple[int, int]) -> None:
        """座標を更新するメソッド
        引数に次に移動したい座標をとり,その座標にプレイヤーの現在座標を更新する.

        Args:
          var1(list) : 次に移動したい座標

        Return:
          なし

        Examples:
          >>> enemy = Enemy(2, 3)
          >>> enemy.update_coordinate((2, 4))
          >>> enemy.now_x
          2
          >>> enemy.now_y
          4

        """
        self.now_x = next_coordinate[0]
        self.now_y = next_coordinate[1]

if __name__ == "__main__":
    doctest.testmod()
