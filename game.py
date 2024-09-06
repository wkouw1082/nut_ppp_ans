import time
import os
from player import Player
from enemy import Enemy
from food import Food
from block import Block
from field import Field
from user_input import UserInput


class Game:
    def __init__(self) -> None:
        """ゲームクラス
        ゲームの初期設定とメインループを実行してゲームを実施するクラス．

        Attributes:
            players (list[Player]): プレイヤーのリスト
            enemies (list[Enemy]): 敵のリスト
            foods (list[Food]): 食べ物のリスト
            blocks (list[Block]): ブロックのリスト
            field (Field): フィールドのインスタンス
        """
        self.players = []
        self.enemies = []
        self.foods = []
        self.blocks = []
        self.field = None
        self.setup()  # ゲームの初期設定
        self.start()  # ゲームのメインループ

    def setup(self) -> None:
        """ゲームの初期設定
        ゲームの初期設定を行うメソッド．
        """
        # フィールドの初期化
        self.players = [Player(3, 3)]
        self.enemies = [Enemy(2, 3), Enemy(1, 4)]
        self.foods = [Food(4, 3)]  # 例としていくつかの食べ物を配置
        # 6*6のフィールドの周りを壁とするBlockインスタンスを生成
        self.blocks = [
            Block(x, y)
            for x in range(6)
            for y in range(6)
            if x == 0 or x == 5 or y == 0 or y == 5
        ]
        self.field = Field(self.players, self.enemies, self.foods, self.blocks)

    def start(self) -> str:
        """ゲームのメインループ
        ゲームのメインループを実行するメソッド．
        キー入力を受け取り，プレイヤーと敵の移動を行い，フィールドを更新する．
        ゲーム終了条件を満たした場合は終了する．
        
        Returns:
            str: ゲーム終了時のメッセージ (例: "Game Over!", "Game Clear!")
        """
        # ゲームのメインループ
        while True:
            os.system("cls" if os.name == "nt" else "clear")  # ターミナルをクリア
            # 動きか方を表示
            print("w: 上に移動")
            print("a: 左に移動")
            print("s: 下に移動")
            print("d: 右に移動")
            #  フィールドを表示
            self.field.display_field()
            # キー入力を受け取る
            key = UserInput.get_user_input()

            player_next_coordinate = self.players[0].move_next(key)
            if self.field.check_bump(
                    player_next_coordinate,
                    list(self.blocks)):
                continue
                # 敵との衝突判定
            if self.field.check_bump(
                    player_next_coordinate,
                    list(self.enemies)):
                print("Game Over!")
                return "Game Over!"
            # 食べ物との衝突判定
            if self.field.check_bump(player_next_coordinate, list(self.foods)):
                self.foods = [
                    food
                    for food in self.foods
                    if food.now_x != player_next_coordinate[0]
                    or food.now_y != player_next_coordinate[1]
                ]
                if not self.foods:
                    print("Game Clear!")
                    return "Game Clear!"

            self.players[0].update_coordinate(player_next_coordinate)

            # 敵の移動
            for enemy in self.enemies:
                enemy_next_coordinate = enemy.move_random()
                if self.field.check_bump(
                        enemy_next_coordinate,
                        list(self.blocks)):
                    continue
                if self.field.check_bump(
                        enemy_next_coordinate,
                        list(self.players)):
                    print("Game Over!")
                    return
                if self.field.check_bump(
                        enemy_next_coordinate,
                        list(self.foods)):
                    continue
                if self.field.check_bump(
                        enemy_next_coordinate,
                        list(self.enemies)):
                    continue

                for other_enemy in self.enemies:
                    if enemy == other_enemy:
                        continue

                    if self.field.check_bump(
                            enemy_next_coordinate,
                            [other_enemy]):
                        continue

                enemy.update_coordinate(enemy_next_coordinate)

            # fieldを更新
            self.field.update_field(
                    self.players,
                    self.enemies,
                    self.foods,
                    self.blocks)

            # 一定の間隔で処理を繰り返す
            # 0.3秒待つ
            time.sleep(0.3)

            # 終了条件のチェック
            # 例えば、全ての食べ物が消えたり、敵とプレイヤーが衝突したりしたら終了する処理を追加する
