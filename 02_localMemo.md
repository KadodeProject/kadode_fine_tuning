# 環境構築(ローカル編)

poetry を使用

poetry では python ファイルの先端に

```
#!/usr/bin/env python
```

をつける必要がある

新規で作る

```
poetry new 名前
```

セットアップ

```
poetry install
```

パッケージ追加

```
poetry add パッケージ名
```

パッケージ更新

```
poetry update
```

実行

```
poetry run python ファイル名
```

or

```
poetry shell
python ファイル名
```

# モデル

# clone してるもの

https://github.com/huggingface/transformers/examples/pytorch/language-modeling/run_clm.py

https://github.com/rinnakk/japanese-pretrained-models

# 参考記事

poetry
https://qiita.com/ksato9700/items/b893cf1db83605898d8a#1-python%E3%81%AE%E3%82%BB%E3%83%83%E3%83%88%E3%82%A2%E3%83%83%E3%83%97

fine-tuning
https://qiita.com/m__k/items/36875fedf8ad1842b729
https://note.com/npaka/n/n8a435f0c8f69
https://developer.mamezou-tech.com/blogs/2022/07/08/gpt-2-japanese/#:~:text=GPT2%2Dmedium%E3%81%A8GPT%2D1b,%E3%81%8B%E3%81%AA%E3%82%8A%E6%B8%9B%E5%B0%91%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%81%99%E3%80%82

wsl で cuda
https://zenn.dev/he/articles/31c922209335b9

poetry で pyTorch
https://ziyixi.science/blog/2022/Poetry-for-ML-on-Cluster/

# メモ

```
torch = [
    {url="https://download.pytorch.org/whl/cu116/torch-1.12.1%2Bcu116-cp310-cp310-linux_x86_64.whl",markers = "sys_platform == 'linux'"},
    {version="^1.12.1",platform = "linux"}]
torchvision = [
    {url="https://download.pytorch.org/whl/cu116/torchvision-0.13.1%2Bcu116-cp310-cp310-linux_x86_64.whl",markers = "sys_platform == 'linux'"},
    {version="^0.13.1",platform = "linux"}]
torchaudio = [
    {url="https://download.pytorch.org/whl/cu116/torchaudio-0.12.1%2Bcu116-cp310-cp310-linux_x86_64.whl",markers = "sys_platform == 'linux'"},
    {version="^0.12.1",platform = "linux"}]
`
```

```

torch = [
{url="https://download.pytorch.org/whl/nightly/cu117/torch-1.14.0.dev20221024%2Bcu117-cp310-cp310-linux_x86_64.whl",markers = "sys_platform == 'linux'"},
{version="^1.12.1",platform = "linux"}]
torchvision = [
{url="https://download.pytorch.org/whl/nightly/cu117/torchvision-0.15.0.dev20221024%2Bcu117-cp310-cp310-linux_x86_64.whl",markers = "sys_platform == 'linux'"},
{version="^0.13.1",platform = "linux"}]
torchaudio = [
{url="https://download.pytorch.org/whl/nightly/cu117/torchaudio-0.14.0.dev20221024%2Bcu117-cp310-cp310-linux_x86_64.whl",markers = "sys_platform == 'linux'"},
{version="^0.12.1",platform = "linux"}]

```

## CUDA のバージョン取得

```
/usr/local/cuda/bin/nvcc -V
```

```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2022 NVIDIA Corporation
Built on Tue_May__3_18:49:52_PDT_2022
Cuda compilation tools, release 11.7, V11.7.64
Build cuda_11.7.r11.7/compiler.31294372_0
```

→

## GPU の情報取得

```
nvidia-smi
```

## PyTorch から確認

```
import torch
torch.cuda.is_available()
#true
print(torch.cuda.get_device_name())
print(torch.cuda.get_device_capability())
```

```
/home/user/.asdf/installs/python/3.10.8/lib/python3.10/site-packages/torch/cuda/__init__.py:146: UserWarning:
NVIDIA GeForce RTX 3070 with CUDA capability sm_86 is not compatible with the current PyTorch installation.
The current PyTorch install supports CUDA capabilities sm_37 sm_50 sm_60 sm_70.
If you want to use the NVIDIA GeForce RTX 3070 GPU with PyTorch, please check the instructions at https://pytorch.org/get-started/locally/
```
