from item import Item
from player import Player
from enemy import Enemy
from item import Item
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
    """

    #  Fieldを生成する関数
    def __init__(self, players, enemies, foods, blocks) -> None:
        self.field = [
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " "],
        ]
        self.players = players
        self.enemies = enemies
        self.food = foods
        self.block = blocks
        # それぞれのアイテムの位置をFieldに反映
        for player in players:
            self.field[player.now_y][player.now_x] = player.icon
        for enemy in enemies:
            self.field[enemy.now_y][enemy.now_x] = enemy.icon
        for food in foods:
            self.field[food.now_y][food.now_x] = food.icon
        for block in blocks:
            self.field[block.now_y][block.now_x] = block.icon

    def update_field(
        self,
        players: list[Player],
        enemies: list[Enemy],
        foods: list[Food],
        blocks: list[Block],
    ) -> list[list[str]]:
        """
        敵、プレイヤー、アイテムを配置を参照して、Fieldを更新する関数
        Args:
            players (list[Player]): プレイヤーのリスト
            enemies (list[Enemy]): 敵のリスト
            items (list[Item]): アイテムのリスト
        Returns:
            list[list[str]]: 更新されたField

        Examples:
            >>> field = Field([Player()], [Enemy()], [()])
            >>> field.update_field([Player()], [Enemy()], [Item()])
            [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        """
        # fieldを#を残して、それ以外は空白にする
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[i][j] != blocks[0].icon:
                    self.field[i][j] = " "
        #  Fieldを更新する処理を記述
        for player in players:
            if player.status:
                self.field[player.now_y][player.now_x] = player.icon
        for enemy in enemies:
            if enemy.status:
                self.field[enemy.now_y][enemy.now_x] = enemy.icon
        for food in foods:
            if food.status:
                self.field[food.now_y][food.now_x] = food.icon

        return self.field

    # 衝突判定を行う関数
    def check_bump(self, next_coordinate: tuple[int, int], items: list[Item]) -> bool:
        """
        2つのアイテムの位置が重なっているか判定する関数
        Args:
            next_coordinate (tuple[int, int]): 次の座標
            items (list[Item]): アイテムのリスト2
        Returns:
            bool: 重なっているかどうか

        Examples:
            >>> field = Field(3, 3, [Player()], [Enemy()], [Item()])
            >>> field.check_bump(Item(), [Item()])
            False
        """
        pass
        # 衝突判定を行う処理を記述
        for item in items:
            if item.now_x == next_coordinate[0] and item.now_y == next_coordinate[1]:
                return True
        return False

    # Fieldを表示する関数
    def display_field(self) -> None:
        """
        Fieldを表示する関数

        Examples:
            >>> field = Field(5, 9, [Player()], [Enemy()], [Item()])
            >>> field.display_field()
            #########
            #P   E  #
            ## #### #
            #       #
            #########
        """
        # self.fieldを表示する処理を記述
        max_width = max(len(row) for row in self.field)  # フィールド内の最大幅を取得

        for row in self.field:
            # 各行の文字列を作成し、不足分を空白文字で埋める
            row_str = "".join(row)
            row_str = row_str.ljust(max_width)
            print(row_str)
