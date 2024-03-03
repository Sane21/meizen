# meizen

## 概要

R7年度大学入試における大学入学共通テストから科目「情報I」が必須科目として追加される。
「情報I」中では大問の一つとしてプログラミングがあり、そこで使用される言語は大学入試センターの定める独自の日本語の言語である。
これを便宜上、DNCL2とする。
本パッケージはDNCL2をPythonにトランスパイルするものである。
Python3の実行環境上で動作するため、Google Colaboratory上での動作や他の既存のPythonのパッケージとの連動が可能である。

パッケージ名称は『大学』に由来する。
> 大学の道は、明徳を明らかにするに在り、民を親しましむるに在り、至善に 止まるに在り
>
> (『大学』一章より 抜粋)

## 導入方法
次のコマンドでインストールできる。
```
pip install git+https://github.com/Sane21/meizen.git
```

## 使用方法
次のコードで{filename}.dnclのDNCL2で記述したファイルをPythonのファイルにトランスパイルすることができる。
```
meizen.make(path, filename)
meizen.build(path, filename)
```
また、次のコードではトランスパイルから実行までを一括で行うことができる。
```
meizen.make_run(path, filename)
meizen.run(path, filename)
```

pathには読み取りたいDNCLファイルのあるフォルダを記述する
filenameには読み取りたいDNCLファイルの名前を記述する ただし拡張子は不要
実行すると、pathのフォルダ内に{filename}.pyが生成される。元からある場合は上書きされる。

※ 2024/03/01 makeは負けを連想させて不適かなと判断し、build, runでも動作するようにしました。従来のコマンドも変わらず動作はします。

本プロジェクトのmeizen/dncl/sample内にサンプルプログラムが存在する。

Google Colaboratory上での運用はipynbファイルを参考にされたい。
