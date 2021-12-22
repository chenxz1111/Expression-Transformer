## Train

```
python main.py [--batch_size] [--epoch] [--num_layers] [--data_set] 
```

## Test

```
python main.py --test_model model_path [--test_data] [--batch_size] [--epoch] [--num_layers] [--data_set] 
```
## CPU

You may train this model on a CPU by deleting all the  `.cuda()` .

## Parameters

You may use these parameters below to obtain the best performance：

| Data | num_layers | epoch | batch_size |
| :---------: | :--------: | :---: | :--------: |
|  bool_expr  |    4/5     |  200  |    400     |
|   bin_cmp   |     4      |  200  |    400     |
|   bin_add   |     4      |  200  |    400     |
|   bin_mul   |     4      |  400  |    400     |
| bin_add_mul |      4      |  400     |     400       |
| bitwise_xor |     2      |  200  |    400     |
| concat | 4 | 100 | 400 |
| rev_concat | 4 | 200 | 400 |

## Results of test

| Data | Baseline | Hint |
| :-------: | :------: | :--: |
| bool_expr |  76.77%  |      |
|  bin_cmp  |  99.30%  |      |
|  bin_add  |  99.60%  |      |
|bin_mul|94.30%||
|bin_add_mul|66.34%||
|bitwise_xor|99.63%||
|concat|99.78%||
|rev_concat|99.97%||

## Results of extra test

| Data | Baseline | Hint |
| :-------: | :------: | :--: |
| bool_expr | - |      |
|  bin_cmp  | 82.21% |      |
|  bin_add  |  66.37% |      |
|bin_mul|53.36%||
|bin_add_mul|27.45%||
|bitwise_xor|70.85%||
|concat|65.45%||
|rev_concat|66.50%||

## Cartesian product (bin_add)

|      |   1    |   2    |   3    |   4    |   5    |
| :--: | :----: | :----: | :----: | :----: | :----: |
|  1   | 99.60% | 62.17% | 29.38% | 9.17%  | 4.17%  |
|  2   | 99.78% | 96.50% | 75.67% | 37.40% | 12.67% |
|  3   | 98.33% | 96.80% | 95.28% | 90.67% | 79.75% |
|  4   | 97.71% | 96.90% | 95.75% | 94.20% | 92.25% |
|  5   | 97.58% | 96.27% | 94.87% | 94.34% | 92.71% |

## bin_mult

|           |   1    |   2    |   3    |   4   |   5   |
| :-------: | :----: | :----: | :----: | :---: | :---: |
| base_line | 48.25% | 23.67% | 11.20% | 1.02% | 0.01% |

