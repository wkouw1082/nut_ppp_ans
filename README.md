# 2024pacman

2024年度の新人研修としてコマンドラインで動くパックマンゲームを作成.


## Requirement
- Python 3.12.2


## Installation
- 結果出力用ディレクトリを作成
```shell
mkdir result
```
- 各種モジュールのインストール
```shell
pip install -r requirements.txt
```


## Usage
- メインプログラムを実行．
  - 出力されるマップ上のP(Player)を動かす方向に(W,A,S,D)を入力します。
```shell
python main.py
```

## Directory Structure
- プロジェクトの構成は以下の通り．
```shell
.
├── config.py           # パラメータ定義
├── main.py             # 実行ファイル
├── item.py             # Enemy,Player,Food,Blockクラスの親クラス
├── block.py            # Blockクラス
├── enemy.py            # Enemyクラス
├── player.py           # Playerクラス
├── food.py             # Foodクラス
├── test_user_input.py  # 入力されたキーを移動方向の座標に変換するファイル
├── controller.py        # エンターキーを押さないでキーから変数に入力できるようにするためのファイル
├── parameters.json     # パラメータ指定用ファイル
├── result              # 結果出力ディレクトリ
│   └── 20211026_165841
└── utils.py            # 共有関数群
```
