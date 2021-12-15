import os
import re

def read_txt(file):
    with open(file, "r") as f:
        data = f.readlines()
        return data

def gen_txt(data, name):
    train_expr = os.path.join('data', 'bool_expr_data', name + '_expr.txt')
    train_res = os.path.join('data', 'bool_expr_data', name + '_res.txt')
    f1 = open(train_expr, 'w')
    f2 = open(train_res, 'w')
    for line in data:
        new_line = line.replace('"', ' ')
        new_line = new_line.replace(')', '  ')
        new_line = new_line.replace('(', '  ')
        new_line = new_line.replace(':', ' : ')
        new_line = new_line.replace(',', ' , ')
        new_line = re.sub('\s+', ' ', new_line)
        new_line = new_line.replace('data 0', 'data0')
        new_line = new_line.replace('data 1', 'data1')
        idx = new_line.index('?=')
        expr = new_line[1:idx-1]
        res = new_line[idx+3:]
        f1.write(expr + '\n')
        f2.write(res + '\n')
        # print(new_line)
        # print(expr)
        # print(res)

    f1.close()
    f2.close()
            
            

train_path = os.path.join('dataset', 'bool_expr_data', 'train.txt')
train_data = read_txt(train_path)
gen_txt(train_data, 'train')

test_path = os.path.join('dataset', 'bool_expr_data', 'test.txt')
test_data = read_txt(test_path)
gen_txt(test_data, 'test')

ext_path = os.path.join('dataset', 'bool_expr_data', 'extra_test.txt')
ext_data = read_txt(ext_path)
gen_txt(ext_data, 'extra_test')