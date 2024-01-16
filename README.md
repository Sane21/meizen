# meizen

## 概要

大学入試センターの定義する大学入学共通テストにて使用されるプログラミング言語DNCLの実行環境としてPythonにトランスコンパイルしこれをGoogle Colaboratory上で動かすものとする。

> 大学の道は、明徳を明らかにするに在り、民を親しましむるに在り、至善に 止まるに在り
>
> (『大学』一章より 抜粋)

## 使い方

pip install git+<https://github.com/Sane21/meizen.git>

meizen.make(path, filename)

pathには読み取りたいDNCLファイルのあるフォルダを記述する
filenameには読み取りたいDNCLファイルの名前を記述する ただし拡張子は不要
実行すると、pathのフォルダ内にfilename.pyが生成される。元からある場合は上書きされる。
