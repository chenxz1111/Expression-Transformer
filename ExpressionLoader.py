import numpy as np
import os

def ExpressionLoader(data):
    path = os.path.join('data', 'bool_expr_data')
    tot_voc = []
    file_list = os.listdir(path)
    for f_name in file_list:
        f = os.path.join(path, f_name)
        with open(f, 'r') as fp:
            lines = fp.readlines()
            for l in lines:
                tot_voc += l.split()
    voc_dic = list(set(tot_voc))
    voc_dic = ['ZERO'] + voc_dic
    if data == 'train':
        expr_file  = os.path.join(path, 'train_expr.txt')
        res_file = os.path.join(path, 'train_res.txt')
        train_data = []
        with open(expr_file) as ef:
            lines = ef.readlines()
            for l in lines:
                vec = l.split()
                train_data.append(([voc_dic.index(w) for w in vec],[]))
        with open(res_file) as rf:
            lines = rf.readlines()
            for i in range(len(lines)):
                vec = lines[i].split()
                for w in vec:
                    train_data[i][1].append(voc_dic.index(w))
        return len(voc_dic), train_data
    elif data == 'test':
        expr_file  = os.path.join(path, 'test_expr.txt')
        res_file = os.path.join(path, 'test_res.txt')
        test_data = []
        with open(expr_file) as ef:
            lines = ef.readlines()
            for l in lines:
                vec = l.split()
                test_data.append(([voc_dic.index(w) for w in vec],[]))
        with open(res_file) as rf:
            lines = rf.readlines()
            for i in range(len(lines)):
                vec = lines[i].split()
                for w in vec:
                    test_data[i][1].append(voc_dic.index(w))
        return len(voc_dic), test_data
    else:
        raise Exception()