import os
import re

def read_txt(file):
    with open(file, "r") as f:
        data = f.readlines()
        return data

def gen_txt_pro(Expression_data, train_data, new_dir):
    dir_path = os.path.join('dataset', new_dir)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    train_expr = os.path.join(dir_path, 'train_expr.txt')
    train_res = os.path.join(dir_path, 'train_res.txt')
    f1 = open(train_expr, 'w')
    f2 = open(train_res, 'w')
    for cnt in range(len(train_data)):
        new_line = train_data[cnt].replace('"', ' ')
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
        if f_name.count('test') > 0:
            new_expr = f_name[:-4] + '_expr' + f_name[-4:]
            new_res = f_name[:-4] + '_res' + f_name[-4:]
            new_expr = os.path.join(dir_path, new_expr)
            new_res = os.path.join(dir_path, new_res)
            f1 = open(new_expr, 'w')
            f2 = open(new_res, 'w')
            f_path = os.path.join(tmp_dir, f_name)
            with open(f_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
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
                        f1.write(expr + '\n')
                        f2.write(res + '\n')
            f1.close()
            f2.close()

def PreProcess_pro(Expression_data):
    dir_name = os.path.join('dataset', Expression_data)
    train_path = os.path.join(dir_name, 'test_2.txt')
    train_data = read_txt(train_path)
    train_data = train_data[:10000]
    gen_txt_pro(Expression_data, train_data, '2')
    for i in range(3, 7):
        train_path = os.path.join(dir_name, 'test_' + str(i) + '.txt')
        train_data = read_txt(train_path)
        train_data = train_data[:640]
        gen_txt_pro(Expression_data, train_data, str(i))
    


PreProcess_pro('bin_add')
