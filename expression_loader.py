import numpy as np
import os

def ExpressionLoader(data, Expression_type):
    path = os.path.join('data', Expression_type)
    expr_tot_voc = []
    res_tot_voc = []
    file_list = os.listdir(path)
    for f_name in file_list:
        if '_expr.txt' in f_name :
            f = os.path.join(path, f_name)
            with open(f, 'r') as fp:
                lines = fp.readlines()
                for l in lines:
                    expr_tot_voc += l.split()
        elif '_res.txt' in f_name :
            f = os.path.join(path, f_name)
            with open(f, 'r') as fp:
                lines = fp.readlines()
                for l in lines:
                    res_tot_voc += l.split()
    expr_voc_dic = sorted(list(set(expr_tot_voc)))
    expr_voc_dic = ['PADDING'] + expr_voc_dic
    res_voc_dic = sorted(list(set(res_tot_voc)))
    res_voc_dic = ['PADDING'] + res_voc_dic + ['START', 'EOS']
    for i ,x in enumerate(expr_voc_dic): print(i,x)
    for i ,x in enumerate(res_voc_dic): print(i,x)
    if data == 'train':
        expr_file  = os.path.join(path, 'train_expr.txt')
        res_file = os.path.join(path, 'train_res.txt')
    elif data.count('test') > 0:
        expr_file  = os.path.join(path, data + '_expr.txt')
        res_file = os.path.join(path, data + '_res.txt')
    else:
        raise Exception()
    expr_data = []
    res_data = []
    expr_max_len = 0
    with open(expr_file) as ef:
        lines = ef.readlines()
        for l in lines:
            vec = l.split()
            expr_max_len = max(expr_max_len, len(vec))
    res_max_len = 0
    with open(res_file) as rf:
        lines = rf.readlines()
        for l in lines:
            vec = l.split()
            res_max_len = max(res_max_len, len(vec))
    with open(expr_file) as ef:
        lines = ef.readlines()
        for l in lines:
            vec = l.split()
            tmp = []
            for w in vec:
                tmp.append(expr_voc_dic.index(w))
            for i in range(expr_max_len - len(vec)):
                tmp.append(0)
            expr_data.append(tmp)
    with open(res_file) as rf:
        lines = rf.readlines()
        for l in lines:
            vec = l.split()
            tmp = []
            for w in vec:
                tmp.append(res_voc_dic.index(w))
            tmp.append(res_voc_dic.index('EOS'))
            for i in range(res_max_len - len(vec)):
                tmp.append(0)
            res_data.append(tmp)
    return len(expr_voc_dic), len(res_voc_dic), expr_data, res_data