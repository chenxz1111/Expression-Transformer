## Dataset Options

You can choose your preferred dataset for this model (using `--data_set` option) from:

```
[
  bool_expr,
  bin_add,
  bin_cmp,
  bin_popcount,
  bin_sub,
  bitwise_and,
  bitwise_not,
  bitwise_or,
  bitwise_xor,
  list_concat,
  list_rev
]
```

## Train

```
python main.py [--batch_size] [--epoch] [--num_layers] [--data_set] 
```

## Test

```
python main.py --test_model model_path [--batch_size] [--epoch] [--num_layers] [--data_set] [--test_data]
```
## Pretrained models

`pretrained_models/`  includes models trained in Megstudio.

```
L: layers num
B: batch size
E: epoch
```

## CPU
Delete all the  `.cuda()` .

## Results of test

|           | Baseline | Space | Hint |
| :-------: | :------: | :---: | :--: |
| bool_expr |  76.77%  |       |      |
|  bin_cmp  |  99.30%  |       |      |
|  bin_add  |  99.60%  |       |      |

## Results of extra test

|           | Baseline | Space | Hint |
| :-------: | :------: | :---: | :--: |
| bool_expr |  |       |      |
|  bin_cmp  | |       |      |
|  bin_add  |  67.80% |       |      |
