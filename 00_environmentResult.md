# 環境選定結果

## 概要

**Google Colab を使うことが最適。**

Google Colab:rinna/japanese-gpt2-medium まで実行できる
usuyuki ローカル:rinna/japanese-gpt2-small まで実行できる

VRAM の容量が一番のボトルネックとなっており、ローカルで実効するより潤沢な VRAM がある Google Colab の方がより強いモデルを使って fine tuning できる。

## Google Colab

- Tesla T4 (VRAM 16GB)
  ※タイミングにより異なる

実行中の様子(rinna/japanese-gpt2-medium)

![colab](https://user-images.githubusercontent.com/63891531/197660412-8c1b2f4f-27a5-4751-9262-f4a019976b9c.png)

## usuyuki 環境

- GeForce RTX 3070 (VRAM 8GB)
- CUDA 11.8

実行中の様子(rinna/japanese-gpt2-small)

![Screenshot 2022-10-25 100033](https://user-images.githubusercontent.com/63891531/197657916-32988ada-773f-4e36-9f44-2676e2496c11.jpg)

## 実行環境に関しての結果

PyTorch の公式には対応していないが、Preview で CUDA11.7 を選ぶと CUDA11.8 でも動く。
ただし、Poetry では URL 指定の pip 的なのが適切にできず依存関係を解消できずエラーになる(上記で示した toml 用のコードを使っても)

Ubuntu on WSL に直で入れると動く。

ただし、GeForce RTX 3070 は VRAM が 8GB しかなく、rinna/japanese-gpt2-medium を読むとアロケーションエラーになる。
結果として rinna/japanese-gpt2-small を使うと 7.3GB くらいに収まり回避できる。
一方で GPU 自体の性能は持て余し倒しており、VRAM 以外使用率 10%にも満たない。完全にメモリ容量がボトルネック。

しかし、Google Colab だと GPU 性能自体は劣るものの、メモリが 10GB 代確保できるため、時間はかかるが rinna/japanese-gpt2-medium も使うことが可能。

結果として Google Colab が最適解となる。
