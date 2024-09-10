from item import Item
from player import Player
from enemy import Enemy
from food import Food
from block import Block


class Field:
    """Fieldクラス
    Fieldクラスは、ゲームのフィールドを表すクラスです。
    プレイヤー、敵、アイテムの位置を更新し、Fieldを表示する機能を持ちます。
    位置を更新する際に衝突判定を行います。

    Attributes:
        players (list[Player]): プレイヤーのリスト
        enemies (list[Enemy]): 敵のリスト
        foods (list[Food]]): アイテムのリスト
        blocks (list[Block]): アイテムのリスト
        field (list[list[str]]): フィールドの情報
        f_size (int): フィールドのサイズ
    """

    #  Fieldを生成する関数
    def __init__(
            self,
            players: list[Player],
            enemies: list[Enemy],
            foods: list[Food],
            blocks: list[Block],
            f_size: int = 6) -> None:
        """
        Fieldクラスの初期化を行う関数

        Args:
            players (list[Player]): プレイヤーのリスト
            enemies (list[Enemy]): 敵のリスト
            foods (list[Food]): アイテムのリスト
            blocks (list[Block]): ブロックのリスト
            f_size (int): フィールドのサイズ
        """
        self.f_size = f_size
        self.field = [["　" for _ in range(f_size)] for _ in range(f_size)]
        self.players = players
        self.enemies = enemies
        self.foods = foods
        self.blocks = blocks
        # それぞれのアイテムの位置をFieldに反映
        self.update_field()

    def update_field(self) -> list[list[str]]:
        """
        敵、プレイヤー、アイテムを配置を参照して、Fieldを更新する関数

        Returns:
            list[list[str]]: 更新されたField

        Examples:
            >>> p = [Player(1, 0)]
            >>> p[0].icon = "p1"
            >>> e1 = Enemy(2, 0)
            >>> e1.icon = "e1"
            >>> e2 = Enemy(1, 1)
            >>> e2.icon = "e2"
            >>> e = [e1, e2]
            >>> f = [Food(0, 1)]
            >>> f[0].icon = "f1"
            >>> b1 = Block(0, 2)
            >>> b1.icon = "b1"
            >>> b2 = Enemy(1, 2)
            >>> b2.icon = "b2"
            >>> b = [b1, b2]
            >>> field = Field(p, e, f, b, 3)
            >>> field.update_field()[0]
            ['\\u3000', 'p1', 'e1']
            >>> field.update_field()[1]
            ['f1', 'e2', '\\u3000']
            >>> field.update_field()[2]
            ['b1', 'b2', '\\u3000']
        """
        # fieldを一旦すべて空白にする
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                self.field[i][j] = "　"
        #  Fieldを更新する処理を記述
        for food in self.foods:
            if food.status:
                self.field[food.now_y][food.now_x] = food.icon
        for enemy in self.enemies:
            if enemy.status:
                self.field[enemy.now_y][enemy.now_x] = enemy.icon
        for block in self.blocks:
            if block.status:
                self.field[block.now_y][block.now_x] = block.icon
        for player in self.players:
            if player.status:
                self.field[player.now_y][player.now_x] = player.icon
        return self.field

    # 衝突判定を行う関数
    def check_bump(
            self,
            target: Item,
            items: list[Item]) -> Item | None:
        """
        2つのアイテムの位置が重なっているか判定する関数

        Args:
            target (Item): アイテム1
            items (list[Item]): アイテムのリスト2

        Returns:
            Item | None: 重なっているアイテムがあればそのアイテム、なければNone

        Examples:
            >>> p = Item(0, 0)
            >>> e = Item(1, 1)
            >>> field = Field([p], [e], [], [])
            >>> p.next_x = 1
            >>> r = field.check_bump(p, [e])
            >>> r is None
            True
            >>> p.next_y = 1
            >>> r = field.check_bump(p, [e])
            >>> r is e
            True
        """
        # 衝突判定を行う処理を記述
        for item in items:
            if item.next_x == target.next_x and item.next_y == target.next_y:
                return item
        return None

    # Fieldを表示する関数
    def display_field(self) -> None:
        """
        Fieldを表示する関数

        Examples:
            >>> p = [Player(1, 0)]
            >>> p[0].icon = "p1"
            >>> e1 = Enemy(2, 0)
            >>> e1.icon = "e1"
            >>> e2 = Enemy(1, 1)
            >>> e2.icon = "e2"
            >>> e = [e1, e2]
            >>> f = [Food(0, 1)]
            >>> f[0].icon = "f1"
            >>> b1 = Block(0, 2)
            >>> b1.icon = "b1"
            >>> b2 = Enemy(1, 2)
            >>> b2.icon = "b2"
            >>> b = [b1, b2]
            >>> field = Field(p, e, f, b, 3)
            >>> field.display_field()
            w: 上に移動
            a: 左に移動
            s: 下に移動
            d: 右に移動
            　p1e1
            f1e2　
            b1b2　
        """
        # 動きか方を表示
        print("w: 上に移動")
        print("a: 左に移動")
        print("s: 下に移動")
        print("d: 右に移動")

        # self.fieldを表示する処理を記述
        max_width = max(len(row) for row in self.field)  # フィールド内の最大幅を取得

        for row in self.field:
            # 各行の文字列を作成し、不足分を空白文字で埋める
            row_str = "".join(row)
            row_str = row_str.ljust(max_width)
            print(row_str)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
