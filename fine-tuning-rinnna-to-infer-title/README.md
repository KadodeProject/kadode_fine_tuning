# 概要

rinna 社のモデルを使って日記の本文からタイトルを生成する言語モデルを usuyuki の日記 2MB 弱で fine-tuning によって作成するプロジェクト。

## fine tuning

```
poetry run python src/run_clm.py \
    --model_name_or_path=rinna/japanese-gpt2-medium \
    --train_file=trainData/gpt2_train_data.txt \
    --validation_file=trainData/gpt2_train_data.txt \
    --do_train \
    --do_eval \
    --num_train_epochs=10 \
    --save_steps=10000 \
    --save_total_limit=3 \
    --per_device_train_batch_size=1 \
    --per_device_eval_batch_size=1 \
    --output_dir=outputModel \
    --use_fast_tokenizer=False
```
