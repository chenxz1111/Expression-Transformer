import os
import re
# file_path = os.path.join('data', 'bin_add_mult_expr_2e4', 'extra_test_expr.txt')

# useless = []

# new_extra_test_expr = os.path.join('data', 'bin_add_mult_expr_2e4', 'new_extra_test_expr.txt')
# new_expr = open(new_extra_test_expr, 'w')
# with open(file_path, 'r') as f:
#     lines = f.readlines()
#     for i in range(len(lines)):
#         sen = lines[i].split()
#         if len(sen) > 400:
#             useless.append(i)
#         else:
#             new_expr.write(lines[i])
# new_expr.close()

# new_res_path = os.path.join('data', 'bin_add_mult_expr_2e4', 'new_extra_test_res.txt')
# new_res = open(new_res_path, 'w')
# file_path = os.path.join('data', 'bin_add_mult_expr_2e4', 'extra_test_res.txt')
# with open(file_path, 'r') as f:
#     lines = f.readlines()
#     for i in range(len(lines)):
#         if i not in useless:
#             new_res.write(lines[i])
# new_res.close()

def print_len(name):
    def txt_len(txt_name):
        train_count = 0
        file_path = os.path.join('data', name, txt_name + '_expr.txt')
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for l in lines:
                sen = l.split()
                train_count += len(sen)
            train_count = train_count / len(lines)

        
        print(txt_name + ':', train_count)
    print(name + ':')
    txt_len('train')
    for i in range(1, 6):
        txt_len('test_' + str(i))
    print('\n')

for i in range(1, 6):
    print_len('new_' + str(i))
# print(len(useless))

# dir_path = os.path.join('dataset', 'bin_add_tmp')
# tgt_dir = os.path.join('dataset', 'bin_add')
# file_list = os.listdir(dir_path)
# for f_name in file_list:
#     count = 0
#     f = os.path.join(dir_path, f_name)
#     tgt_fname = os.path.join(tgt_dir, f_name)
#     tgt_f = open(tgt_fname, 'w')
#     with open(f, 'r') as fp:
#         lines = fp.readlines()
#         for line in lines:
#             new_line = line.replace('"', ' ')
#             new_line = new_line.replace('bin-mult', ' ')
#             new_line = new_line.replace(')', ' ) ')
#             new_line = new_line.replace('(', ' ( ')
#             new_line = new_line.replace(':', ' : ')
#             new_line = new_line.replace(',', ' , ')
#             new_line = re.sub('\s+', ' ', new_line)
#             new_line = new_line.replace('data 0', 'data0')
#             new_line = new_line.replace('data 1', 'data1')
#             idx = new_line.index('?=')
#             expr = new_line[1:idx-1]
#             if len(expr) > 900:
#                 count += 1
#             else:
#                 tgt_f.write(new_line + '\n')
#     tgt_f.close()            
#     print(count)

def dataset():
    for i in range(1, 6):
        dir_path = os.path.join('dataset', 'bin_mult_2e4_v' + str(i))
        tgt_dir = os.path.join('dataset', 'mult_new_' + str(i))
        if not os.path.exists(tgt_dir):
            os.makedirs(tgt_dir)
        count = 0   
        f = os.path.join(dir_path, 'train.txt')
        tgt_fname = os.path.join(tgt_dir, 'train.txt')
        tgt_f = open(tgt_fname, 'w')
        with open(f, 'r') as fp:
            lines = fp.readlines()
            for line in lines:
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
                if len(expr) > 900:
                    count += 1
                else:
                    tgt_f.write(new_line + '\n')
        tgt_f.close()            
        print(count)
    for i in range(1, 6):
        dir_path = os.path.join('dataset', 'bin_mult_2e4_v' + str(i))
        for j in range(1, 6): 
            tgt_dir = os.path.join('dataset', 'mult_new_' + str(j))
            if not os.path.exists(tgt_dir):
                os.makedirs(tgt_dir)
            count = 0   
            f = os.path.join(dir_path, 'extra_test.txt')
            tgt_fname = os.path.join(tgt_dir, 'test_' + str(i) +'.txt')
            tgt_f = open(tgt_fname, 'w')
            with open(f, 'r') as fp:
                lines = fp.readlines()
                for line in lines:
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
                    if len(expr) > 900:
                        count += 1
                    else:
                        tgt_f.write(new_line + '\n')
            tgt_f.close()            
            print(count)

def read_txt(file):
    with open(file, "r") as f:
        data = f.readlines()
        return data

def gen_txt_pro( train_data, new_dir):
    dir_path = os.path.join('data', new_dir)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    train_expr = os.path.join(dir_path, 'train_expr.txt')
    train_res = os.path.join(dir_path, 'train_res.txt')
    f1 = open(train_expr, 'w')
    f2 = open(train_res, 'w')
    for cnt in range(len(train_data)):
        new_line = train_data[cnt].replace('"', ' ')
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
    f1.close()
    f2.close()

    tmp_dir =  os.path.join('dataset', new_dir)
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
            f1.close()
            f2.close()

# dataset()

# for i in range(1, 6):
#     dir_name = os.path.join('dataset', 'mult_new_' + str(i))
#     train_path = os.path.join(dir_name, 'train.txt')
#     train_data = read_txt(train_path)
#     train_data = train_data[:15000]
#     gen_txt_pro(train_data, 'mult_new_' + str(i))