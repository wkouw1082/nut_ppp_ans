import time
from player import Player
from enemy import Enemy
from food import Food
from block import Block
from field import Field
from user_input import UserInput
from config import Parameters
from random import randint
import logging
import os


logger = logging.getLogger(__name__)


class Game:
    """ゲームクラス
    ゲームの初期設定とメインループを実行してゲームを実施するクラス．

    Attributes:
        players (list[Player]): プレイヤーのリスト
        enemies (list[Enemy]): 敵のリスト
        foods (list[Food]): 食べ物のリスト
        blocks (list[Block]): ブロックのリスト
        field (Field): フィールドのインスタンス
    """

    def __init__(self, params: Parameters) -> None:
        """ゲームクラスの初期化

        Args:
            params (Parameters): configのパラメータのインスタンス
        """
        self.players = []
        self.enemies = []
        self.foods = []
        self.blocks = []
        self.field = None
        self.setup(params)  # ゲームの初期設定
        self.start()  # ゲームのメインループ

    def setup(self, params: Parameters) -> None:
        """ゲームの初期設定
        ゲームの初期設定を行うメソッド．

        Args:
            params (Parameters): configのパラメータのインスタンス
        """
        f_size = params.field_size  # フィールドのサイズ
        e_num = params.enemy_num
        f_num = params.food_num
        # フィールドの初期化
        self.players = [Player(1, 1)]
        self.enemies = [
            Enemy(randint(1, f_size - 2), randint(1, f_size - 2))
            for _ in range(e_num)]
        self.foods = [
            Food(randint(1, f_size - 2), randint(1, f_size - 2))
            for _ in range(f_num)
            ]  # 食べ物を配置
        # 6*6のフィールドの周りを壁とするBlockインスタンスを生成
        if f_size < 4:
            raise ValueError("field_size must be greater than 4")
        self.blocks = [
            Block(x, y)
            for x in range(f_size)
            for y in range(f_size)
            if x == 0 or x == f_size - 1 or y == 0 or y == f_size - 1
        ]
        self.field = Field(
            self.players,
            self.enemies,
            self.foods,
            self.blocks,
            f_size)

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
            #  フィールドを表示
            os.system("cls" if os.name == "nt" else "clear")  # ターミナルをクリア
            self.field.display_field()

            # プレイヤーの移動を決定
            for player in self.players:
                # キー入力を受け取る
                key = UserInput.get_user_input()
                player.get_next_pos(key)

            # 敵の移動を決定
            for enemy in self.enemies:
                enemy.get_next_pos()

            # プレイヤーと敵の移動
            for item in self.players + self.enemies:
                # ブロックとの衝突判定
                bumped_item = self.field.check_bump(item, list(self.blocks))
                if bumped_item is not None:
                    item.update_pos(stuck=True)
                else:
                    item.update_pos()

            for player in self.players:
                # 敵との衝突判定
                if self.field.check_bump(player, list(self.enemies)):
                    player.change_face_bad()
                    self.field.update_field()
                    os.system("cls" if os.name == "nt" else "clear")
                    # ターミナルをクリア
                    self.field.display_field()
                    logger.info("Game Over!")
                    return "Game Over!"

                # 食べ物との衝突判定
                bumped_item = self.field.check_bump(player, list(self.foods))
                if bumped_item is not None:
                    bumped_item.status = False
                    if all([not food.status for food in self.foods]):
                        player.change_face_good()
                        self.field.update_field()
                        os.system("cls" if os.name == "nt" else "clear")
                        # ターミナルをクリア
                        self.field.display_field()
                        logger.info("Game Clear!")
                        return "Game Clear!"

            # fieldを更新
            self.field.update_field()

            # 一定の間隔で処理を繰り返す
            # 0.3秒待つ
            time.sleep(0.3)

            # 終了条件のチェック
            # 例えば、全ての食べ物が消えたり、敵とプレイヤーが衝突したりしたら終了する処理を追加する
