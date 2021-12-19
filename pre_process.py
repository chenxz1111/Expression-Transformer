import os
import re

def read_txt(file):
    with open(file, "r") as f:
        data = f.readlines()
        return data

def gen_bool_txt(Expression_data, data, name):
    dir_name = os.path.join('data', Expression_data)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    train_expr = os.path.join('data', Expression_data, name + '_expr.txt')
    train_res = os.path.join('data', Expression_data, name + '_res.txt')
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

def gen_cmp_txt(Expression_data, data, name):
    dir_name = os.path.join('data', Expression_data)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    train_expr = os.path.join('data', Expression_data, name + '_expr.txt')
    train_res = os.path.join('data', Expression_data, name + '_res.txt')
    f1 = open(train_expr, 'w')
    f2 = open(train_res, 'w')
    for line in data:
        new_line = line.replace('"', ' ')
        new_line = new_line.replace('bin-cmp', ' ')
        new_line = new_line.replace(')', ' ) ')
        new_line = new_line.replace('(', ' ( ')
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

def gen_xor_txt(Expression_data, data, name):
    dir_name = os.path.join('data', Expression_data)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    train_expr = os.path.join('data', Expression_data, name + '_expr.txt')
    train_res = os.path.join('data', Expression_data, name + '_res.txt')
    f1 = open(train_expr, 'w')
    f2 = open(train_res, 'w')
    for line in data:
        new_line = line.replace('"', ' ')
        new_line = new_line.replace('bitwise-xor', ' ')
        new_line = new_line.replace(')', ' ) ')
        new_line = new_line.replace('(', ' ( ')
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

def gen_mult_txt(Expression_data, data, name):
    dir_name = os.path.join('data', Expression_data)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    train_expr = os.path.join('data', Expression_data, name + '_expr.txt')
    train_res = os.path.join('data', Expression_data, name + '_res.txt')
    f1 = open(train_expr, 'w')
    f2 = open(train_res, 'w')
    for line in data:
        new_line = line.replace('"', ' ')
        new_line = new_line.replace('bin-mult', ' ')
        new_line = new_line.replace(')', ' ) ')
        new_line = new_line.replace('(', ' ( ')
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

def gen_add_txt(Expression_data, data, name):
    dir_name = os.path.join('data', Expression_data)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    train_expr = os.path.join('data', Expression_data, name + '_expr.txt')
    train_res = os.path.join('data', Expression_data, name + '_res.txt')
    f1 = open(train_expr, 'w')
    f2 = open(train_res, 'w')
    for line in data:
        new_line = line.replace('"', ' ')
        new_line = new_line.replace('bin-add', ' ')
        new_line = new_line.replace(')', ' ) ')
        new_line = new_line.replace('(', ' ( ')
        new_line = new_line.replace(':', ' : ')
        new_line = new_line.replace(',', ' , ')
        new_line = re.sub('\s+', ' ', new_line)
        new_line = new_line.replace('data 0', 'data0')
        new_line = new_line.replace('data 1', 'data1')
        idx = new_line.index('?=')
        expr = new_line[1:idx-1]
        res = new_line[idx+3:]
        if len(expr) < 900:
            f1.write(expr + '\n')
            f2.write(res + '\n')
        # print(new_line)
        # print(expr)
        # print(res)
    f1.close()
    f2.close()

def gen_add_mult_txt(Expression_data, data, name):
    dir_name = os.path.join('data', Expression_data)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    train_expr = os.path.join('data', Expression_data, name + '_expr.txt')
    train_res = os.path.join('data', Expression_data, name + '_res.txt')
    f1 = open(train_expr, 'w')
    f2 = open(train_res, 'w')
    for line in data:
        new_line = line.replace('"', ' ')
        new_line = new_line.replace(')', ' ) ')
        new_line = new_line.replace('(', ' ( ')
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

def gen_txt(Expression_data, data, name):
    if Expression_data == 'bool_20000':
        gen_bool_txt(Expression_data, data, name)
    elif Expression_data == 'bin_cmp':
        gen_cmp_txt(Expression_data, data, name)
    elif Expression_data == 'bin_cmp_2e4':
        gen_cmp_txt(Expression_data, data, name)
    elif Expression_data == 'bitwise_xor_2e4':
        gen_xor_txt(Expression_data, data, name)
    elif Expression_data == 'bin_mult_2e4':
        gen_mult_txt(Expression_data, data, name)
    elif Expression_data == 'bin_add_2e4':
        gen_add_txt(Expression_data, data, name)
    elif Expression_data == 'bin_add_tmp':
        gen_add_txt(Expression_data, data, name)
    elif Expression_data == 'bin_add_mult_expr_2e4':
        gen_add_mult_txt(Expression_data, data, name)

def PreProcess(Expression_data):
    train_path = os.path.join('dataset', Expression_data, 'train.txt')
    train_data = read_txt(train_path)
    gen_txt(Expression_data, train_data, 'train')

    test_path = os.path.join('dataset', Expression_data, 'test.txt')
    test_data = read_txt(test_path)
    gen_txt(Expression_data, test_data, 'test')

    ext_path = os.path.join('dataset', Expression_data, 'extra_test.txt')
    ext_data = read_txt(ext_path)
    gen_txt(Expression_data, ext_data, 'extra_test')


def gen_txt_tmp(Expression_data, data, name, train_data):
    dir_name = os.path.join('data', Expression_data)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    train_expr = os.path.join('data', Expression_data, name + '_expr.txt')
    train_res = os.path.join('data', Expression_data, name + '_res.txt')
    f1 = open(train_expr, 'w')
    f2 = open(train_res, 'w')
    for line in data:
        if line not in train_data:
            new_line = line.replace('"', ' ')
            new_line = new_line.replace('bin-add', ' ')
            new_line = new_line.replace(')', ' ) ')
            new_line = new_line.replace('(', ' ( ')
            new_line = new_line.replace(':', ' : ')
            new_line = new_line.replace(',', ' , ')
            new_line = re.sub('\s+', ' ', new_line)
            new_line = new_line.replace('data 0', 'data0')
            new_line = new_line.replace('data 1', 'data1')
            idx = new_line.index('?=')
            expr = new_line[1:idx-1]
            res = new_line[idx+3:]
            if len(expr) < 900:
                f1.write(expr + '\n')
                f2.write(res + '\n')
            # print(new_line)
            # print(expr)
            # print(res)
    f1.close()
    f2.close()

def PreProcess_tmp(Expression_data):
    train_path = os.path.join('dataset', Expression_data, 'train.txt')
    train_data = read_txt(train_path)
    gen_txt(Expression_data, train_data, 'train')

    for i in range(1, 7):
        test_path = os.path.join('dataset', Expression_data, 'test_'+ str(i) + '.txt')
        test_data = read_txt(test_path)
        gen_txt_tmp(Expression_data, test_data, 'test_' + str(i), train_data)


def gen_txt_pro(Expression_data, train_data, new_dir, max_len):
    dir_path = os.path.join('data', new_dir)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    train_expr = os.path.join(dir_path, 'train_expr.txt')
    train_res = os.path.join(dir_path, 'train_res.txt')
    f1 = open(train_expr, 'w')
    f2 = open(train_res, 'w')
    for cnt in range(len(train_data)):
        if(cnt < max_len):
            new_line = lines[cnt].replace('"', ' ')
            new_line = new_line.replace('bin-add', ' ')
            new_line = new_line.replace(')', ' ) ')
            new_line = new_line.replace('(', ' ( ')
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
    f1.close()
    f2.close()

    tmp_dir =  os.path.join('dataset', Expression_data)
    f_list = os.listdir(tmp_dir)
    for f_name in f_list:
        pass

def PreProcess_pro(Expression_data):
    train_path = os.path.join('dataset', Expression_data, 'train.txt')
    train_data = read_txt(train_path)
    gen_txt_pro(Expression_data, train_data, '2', 10000)

# PreProcess('bool_20000')
# PreProcess('bin_cmp_2e4')
# PreProcess('bitwise_xor_2e4')
# PreProcess('bin_mult_2e4')
# PreProcess('bin_add_2e4')
# PreProcess('bin_add_mult_expr_2e4')
PreProcess_tmp('bin_add')