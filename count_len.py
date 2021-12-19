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

# count = 0
# file_path = os.path.join('data', 'bin_add_mult_expr_2e4', 'new_extra_test_expr.txt')
# with open(file_path, 'r') as f:
#     lines = f.readlines()
#     for l in lines:
#         sen = l.split()
#         if len(sen) > 400:
#             count += 1

# print(count)


# print(len(useless))

dir_path = os.path.join('dataset', 'bin_add_tmp')
tgt_dir = os.path.join('dataset', 'bin_add')
file_list = os.listdir(dir_path)
for f_name in file_list:
    count = 0
    f = os.path.join(dir_path, f_name)
    tgt_fname = os.path.join(tgt_dir, f_name)
    tgt_f = open(tgt_fname, 'w')
    with open(f, 'r') as fp:
        lines = fp.readlines()
        for line in lines:
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
            if len(expr) > 900:
                count += 1
            else:
                tgt_f.write(new_line + '\n')
    tgt_f.close()            
    print(count)