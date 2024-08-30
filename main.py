import os
from field import Field
from user_input import UserInput
import time
from player import Player
from enemy import Enemy
from food import Food
from block import Block


def main() -> None:
    # フィールドの初期化
    players = [Player(3, 3)]
    enemies = [Enemy(2, 3), Enemy(1, 4)]
    foods = [Food(4, 3)]  # 例としていくつかの食べ物を配置
    # 6*6のフィールドの周りを壁とするBlockインスタンスを生成
    blocks = [
        Block(x, y)
        for x in range(6)
        for y in range(6)
        if x == 0 or x == 5 or y == 0 or y == 5
    ]
    field = Field(players, enemies, foods, blocks)

    # ゲームのメインループ
    while True:
        os.system("cls" if os.name == "nt" else "clear")  # ターミナルをクリア
        # 動きか方を表示
        print("w: 上に移動")
        print("a: 左に移動")
        print("s: 下に移動")
        print("d: 右に移動")
        #  フィールドを表示
        field.display_field()
        # キー入力を受け取る
        key = UserInput.get_user_input()

        player_next_coordinate = players[0].move_next(key)
        if field.check_bump(player_next_coordinate, list(blocks)):
            continue
            # 敵との衝突判定
        if field.check_bump(player_next_coordinate, list(enemies)):
            print("Game Over!")
            return
        # 食べ物との衝突判定
        if field.check_bump(player_next_coordinate, list(foods)):
            foods = [
                food
                for food in foods
                if food.now_x != player_next_coordinate[0]
                or food.now_y != player_next_coordinate[1]
            ]
            if not foods:
                print("Game Clear!")
                return

        players[0].update_coordinate(player_next_coordinate)

        # 敵の移動
        for enemy in enemies:
            enemy_next_coordinate = enemy.move_random()
            if field.check_bump(enemy_next_coordinate, list(blocks)):
                continue
            if field.check_bump(enemy_next_coordinate, list(players)):
                print("Game Over!")
                return
            if field.check_bump(enemy_next_coordinate, list(foods)):
                continue
            if field.check_bump(enemy_next_coordinate, list(enemies)):
                continue

            for other_enemy in enemies:
                if enemy == other_enemy:
                    continue

                if field.check_bump(enemy_next_coordinate, [other_enemy]):
                    continue

            enemy.update_coordinate(enemy_next_coordinate)

        # fieldを更新
        field.update_field(players, enemies, foods, blocks)

        # 一定の間隔で処理を繰り返す
        # 0.3秒待つ
        time.sleep(0.3)

        # 終了条件のチェック
        # 例えば、全ての食べ物が消えたり、敵とプレイヤーが衝突したりしたら終了する処理を追加する


if __name__ == "__main__":
    main()
