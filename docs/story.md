# 可視化しながら学ぶ天文学（恒星の基本編）
サークルの発表で使う星表可視化のネタ帳。内容はあまりまとめる気ない。

## 星表
### 天体カタログ（astronomical catalog）
天体カタログとは、特定種類の天体や観測方法に従ってまとめられた表のこと。中でも恒星のカタログは星表と呼ばれる。掃天観測(astronomical survey、ローラー作戦で星を観測していくこと)の成果物として発表されることが多い。
メシエ天体とか、NGCとかみんな聞いたことあると思う。

### ヒッパルコス星表


## 星図に落とし込む
車輪の再発明。コスパ悪いって批判は認める。

### 等級を表現
#### 見かけの等級
##### 視等級
##### 写真等級とUBVシステム
#### 絶対等級
##### 距離（パーセク）
### 色をつける
#### B-V色指標
色をつけたはいいけど、なんか微妙。。。
明度の調整がうまくいっていないため失敗。
#### スペクトル

## 散布図にする
せっかくヒッパルコス星表から等級と色を取り出すことができたので、とりあえず並べてみる。
### HR図
### 恒星進化論
#### 原始星
#### 主系列星
http://spaceinfo.jaxa.jp/ja/main_sequence.html
http://www.astronomy.orino.net/site/kataru/galaxy/stellar_evolution/main_sequence_stars.html
#### 赤色巨星
#### 白色矮星

## まとめ
車輪の再発明をすることで、恒星についての理解は深まった気がする。
比較的最近のデータを使ったとはいえ、実は天文学の発達をなぞった内容にもなっている。
ライフハック的に枝葉の知識を得るのもいいけど、たまには車輪の再発明もいいもんだよ。
枝葉の知識だけだと、アップデートを忘れた次の瞬間に詰む。

あ、ヒッパルコス星表から星図へのマッピングは失敗だね。

## 参考文献
- 天体カタログ
    - 『フリー百科事典　ウィキペディア日本語版』（http://ja.wikipedia.org/）
    - 
- 掃天観測（そうてんかんそく、英語: astronomical survey、スカイサーベイとも）は、望遠鏡を用いて一定範囲の夜空を観測することをいう。特定の天体を観測する指向観測と対をなす概念である




# 視等級
実際に目で見たときの星の明るさ(等級)のこと。通常、等級といえばこの視等級をいう。
写真撮影時の等級(写真等級)や絶対等級と区別するために、こう呼ぶ。
(観測者からみた等級のこと？)

# 等級と測光システム
みんなが好き勝手に等級を定義してしまうと大変なので、統一的な等級と測定方法をセットで定義したのが測光システム。
測光システムにはジョンソンシステム、ガンシステムなど、いろいろな種類があるけど、今回はジョンソンシステムのみを紹介。

## ジョンソンシステム
ジョンソンのUBVシステム及びそれを拡張したジョンソン-カズンズのUBVRI測光システムを指します。現時点において標準的な測光システムです。
こと座のベガが等級の基準って話を聞いたことがある人もいると思いますが、この測光システムにおいては、ベガが0等級となるのは単なる偶然。（そういえばベガってどれだっけ？）

### UBVシステム
狭義のジョンソンシステム。ジョンソンUBVシステム。三色測光ともいう。

- U:紫外線等級(ultra violet)
    - 紫外に感度のピーク(中心波長360nm、波長幅70nm)がある等級
- B:青色等級(blue)
    - 可視光線の青色付近にピーク(中心波長440nm、波長幅100nm)がある等級
- V:視等級(visual)
    - 緑-黄色付近にピーク(中心波長550nm、波長幅90nm)がある等級
    - 人の目にもっとも感じる波長なのでvisual

### RIシステム
カズンズRIシステム。赤や赤外線に特化した測光システム。低波長の光を表現できないジョンソンUBVシステムの拡張としても利用される。

- R:赤色等級(red)
    - 可視光線の赤色付近にピーク(中心波長700nm、波長幅220nm)がある等級
- I:赤外線等級(infrared)
    - 赤外線領域にピーク(中心波長880nm、波長幅240nm)がある等級
    - infra:下側にある(vs ultra:上側にある)

# 参考文献
市川隆(1997年)「標準測光システム」天文月報　第90巻　第1号
http://www.asj.or.jp/geppou/archive_open/1997/pdf/19970103c.pdf

SBIGJapan（国際光器/株式会社マゼラン）
光電測光専用フィルター「ジョンソン U・B・V・R・I 」
http://www.sbig-japan.com/UBVRI/ubvri_m.html

# スペシャルサンクス
- いばーさん


# 測光観測
主に天体の明るさを測定するための観測のこと。測光時にフィルターを通すことで大まかな色の情報も得ることができる。
# 分光観測
天体からの光を波長ごとに分けて（分光して）、スペクトルを取得する観測のこと。
# 色指数
測光システムにより定義される異なるバンドで測定された等級の差のこと。
短い波長帯での等級から長い波長帯での等級を引いた値。色指数が小さいほど高温、大きいほど低温。

```
1. 点をうつ
(*^◯^*)「よくわからないけど、きっとすごいんだ！」
2. 等級をあらわす
視等級の説明
(*^◯^*)「イケるやん」
3. 色をつける
B-V色指数
UBVシステム
(ヽ*´○`*)「...(アカン)」

1. 視等級の散布図
(*^◯^*)「よくわからないんだ！」
2. 絶対等級の散布図
(*^◯^*)「なんか傾向が見えてきたんだ！」

1. おわり
＼横浜優勝／
```

