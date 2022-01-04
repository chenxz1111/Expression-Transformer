## The Performance of Expression Evaluation on Transformer

Expression evaluation is a kind of reasoning problem, which contains many different specific tasks. We design a new data set, which contains some different examples of expression evaluation tasks, and the model needs to learn to respond to the task through each example of the task.

The innovation of this work consists of three parts:

* We came up with new tasks, new data sets.

* We test the performance of the model on different tasks and explore its generalization power as the data size changes.

* In some expression evaluation tasks, we added annotation of intermediate results at the end of data, and tested whether the accuracy of the model could be greatly improved compared with data without annotation of intermediate results.

You may check our reports for more details. 

## Train

```
python main.py [--batch_size] [--epoch] [--num_layers] [--data_set] 
```

## Test

```
python main.py --test_model model_path [--test_data] [--batch_size] [--epoch] [--num_layers] [--data_set] 
```

## Hint

You may create a folder `/model` to obtain your models or pretrained models.

data_set : The type of data you want to train or test this model on, usually the folder's name under `/data`.

test_data : The test data of your model, usually named 'test' or 'extra_test'.

test_model : The path of the model you want to test. 

## CPU

You may train this model on a CPU by **deleting all the  `.cuda()` .**

## Parameters

You may use these parameters below to obtain the best performance：

| Data        | num_layers | epoch | batch_size |
|:-----------:|:----------:|:-----:|:----------:|
| bool_expr   | 4/5        | 200   | 400        |
| bin_cmp     | 4          | 200   | 400        |
| bin_add     | 4          | 200   | 400        |
| bin_mul     | 4          | 400   | 400        |
| bin_add_mul | 4          | 400   | 400        |
| bitwise_xor | 2          | 200   | 400        |
| concat      | 4          | 100   | 400        |
| rev_concat  | 4          | 200   | 400        |

## Results

You can obtain our results in our report.

## Reference

https://colab.research.google.com/drive/1g4ZFCGegOmD-xXL-Ggu7K5LVoJeXYJ75
