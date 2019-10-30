# star-map-sample
サークルの発表で使う星表可視化のネタ帳。内容はあまりまとめる気ない。

## 起動方法
```bash
$ python3 -m http.server 8001
```

`http://localhost:8001/sample.html` にアクセス。

# やりたいこと
自分で星図をつくる。データを可視化する過程で必要になる知識をまとめてネタとして仕込む。

飽きっぽい性格だから、スモールステップで進めていく。途中で投げ出したらごめん。

1. なにはともあれ最初は星表のフィルタリング
2. まずは星図を作ってみる
3. 等級を表現する
4. 色を表現する
5. 色と等級の散布図を作る（HR図。ここで絶対等級をからめる）

このステップで必要なさそうな技術はオーバースペックなので使いません。
というか、必要以上に僕のPCを汚したくないし、APサーバも立てたくない。

## 星表の準備と加工
### 項目
全部で78項目もありますが、僕にはオーバースペック。使うのは以下の5項目。

| 項目名     | カラム位置 | 説明                                                                    |
|:-----------|--------:|:------------------------------------------------------------------------|
| HIP_Number |       1 | HIPのID                                                                  |
| Vmag       |       5 | 実視域の等級。ジョンソンのUBVシステムによる測定値。`V`は実視域を示すVisual、`Mag`はMagnitude |
| RA_Deg     |       8 | 赤経（せきけい、right ascension）単位は`度`                                     |
| Dec_Deg    |       9 | 赤緯（せきい、declination）単位は`度`                                          |
| Parallax   |      11 | 視差角。単位は`ミリ秒`                                                      |
| BV_Color   |      37 | B-V色指数                                                               |

ちなみに、カラム位置は０発進。

## まずは星図をつくってみる
D3.js を使って描画します。説明は割愛。
ドラグナーじゃないよ。

## なにはともあれ最初は星表のフィルタリング
118,218星もあるので、適当な等級でフィルタリングしないと描画しきれなさそうです。さすがに限界等級が12.4等（精度が出ているのは9等以上の星）にもなると、量が半端ない。
そのうち範囲検索したりする可能性も考慮してDBで管理したほうがいいのは間違いないんだけど、 **プライベートのPCにDBなんか入れたくない。** 
せめてDockerみたいなポータブルな環境を用意できればいいんだけど、プロトタイプの位置付け ~~（正直めんどくさい）~~ なので今回は割愛。

Use the Index ... Luke....

まぁ、等級については今更語らなくてもいいですよね。

今回は人間が肉眼で見える限界が6.5等級くらいらしいので、6.5等級まででフィルタリングします。それでも8,874件とうデータ量。
ちなみに、僕はいつも酔っ払っているので、2等級も見れないです。セルフ東京の夜空。星座がわかりやすい。

### 色をRGBで表現したい
いきなりB-V色指数とか言われても、どんな色をしているのかよくわかりません。
なので、なんkとかわかりやすい色（RGB）に変換したいです。
正確ではありませんが、色温度に変換し、そこからRGBに置き換えます。

って思ったけど、B-V色指数と色の相関で決め打ちで色を出すに止める。

![B-V 色指数の値と対応する色](https://astro-dic.jp/wp/wp-content/uploads/color_index-2.gif)  
出典：公益社団法人 日本天文学会 天文辞典

## 
