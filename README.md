# これはなに？ 
これはctf問題作成用のプログラムのあれこれです  

## RandStr.py
- 機能
  - -h: ヘルプを表示する
  - -f: ファイル名を指定して出力 (デフォルトは"question.txt")
  - -k: 隠す文字列を指定する (デフォルトは"CTFKIT{well done}")
  - -x: ランダムに生成する文字列の1行あたりの長さを指定する (デフォルトは1000文字)
  - -y: ランダムに生成する文字列の行数を指定する (デフォルトは1000文字)
- ex.
  - `$python RandStr.py`
  - `$python RandStr.py -h`
  - `$python RandStr.py -f hoge.txt -k "{Hello,World}" -x 500 -y 500`  

## kanjibf.py
brainf\*\*kのシンボルに漢字を当てはめたものです.
|  bf  | kbf  |
| ---- | ---- |
|  >   |  右  |
|  <   |  左  |
|  +   |  増  |
|  -   |  減  |
|  .   |  出  |
|  ,   |  入  |
|  [   |  始  |
|  ]   |  終  |
  
オプションなしで実行すると対話形式(?)でスタートします  
入力したbrainf\*\*を漢字brainf\*\*に変換してout.kbfに保存します  

- 機能
	- ファイル名.bf: brainf\*\*kで書かれたファイルを指定する
- ex.
	- `$python kanjibf.py text.bf`
