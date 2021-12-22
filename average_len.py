import os
import re
# ori = os.path.join('data', 'bin_mult_2e4', 'train_expr.txt')
# with open(ori, 'r') as f:
#     lines = f.readlines()
#     cpt_len = 0
#     for l in lines:
#         cpt_len += len(l)
#     print(cpt_len / len(lines))

# for i in range(1, 6) :
#     ori = os.path.join('data', 'mult_new_' + str(i), 'train_expr.txt')
#     with open(ori, 'r') as f:
#         lines = f.readlines()
#         cpt_len = 0
#         for l in lines:
#             cpt_len += len(l)
#         print(cpt_len / len(lines))

dir_path = os.path.join('dataset', 'bool_expr')
tgt_dir = os.path.join('dataset', 'bool_expr' )
# if not os.path.exists(tgt_dir):
#     os.makedirs(tgt_dir)
# count = 0   
f = os.path.join(dir_path, 'new_extra_test.txt')
# tgt_fname = os.path.join(tgt_dir, 'new_extra_test.txt')
# tgt_f = open(tgt_fname, 'w')
with open(f, 'r') as fp:
    train_data = fp.readlines()
#     for line in lines:
#         new_line = line.replace('"', ' ')
#         new_line = new_line.replace('bin-mult', ' ')
#         new_line = new_line.replace(')', ' ) ')
#         new_line = new_line.replace('(', ' ( ')
#         new_line = new_line.replace(':', ' : ')
#         new_line = new_line.replace(',', ' , ')
#         new_line = re.sub('\s+', ' ', new_line)
#         new_line = new_line.replace('data 0', 'data0')
#         new_line = new_line.replace('data 1', 'data1')
#         idx = new_line.index('?=')
#         expr = new_line[1:idx-1]
#         if len(expr) > 400:
#             count += 1
#         else:
#             tgt_f.write(new_line + '\n')
# tgt_f.close()            
# print(count)



dir_path = os.path.join('data', 'bool_expr')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
train_expr = os.path.join(dir_path, 'new_extra_expr.txt')
train_res = os.path.join(dir_path, 'new_extra_res.txt')
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