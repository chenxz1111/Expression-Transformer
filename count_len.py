import os

file_path = os.path.join('data', 'bin_add_mult_expr_2e4', 'train_expr.txt')

useless = []

new_train_expr = os.path.join('data', 'bin_add_mult_expr_2e4', 'new_train_expr.txt')
new_expr = open(new_train_expr, 'w')
with open(file_path, 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        sen = lines[i].split()
        if len(sen) > 400:
            useless.append(i)
        else:
            if len(useless) < 108 :
                useless.append(i)
            else:
                new_expr.write(lines[i])
new_expr.close()

new_res_path = os.path.join('data', 'bin_add_mult_expr_2e4', 'new_train_res.txt')
new_res = open(new_res_path, 'w')
file_path = os.path.join('data', 'bin_add_mult_expr_2e4', 'train_res.txt')
with open(file_path, 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if i not in useless:
            new_res.write(lines[i])
new_res.close()

count = 0
file_path = os.path.join('data', 'bin_add_mult_expr_2e4', 'new_train_expr.txt')
with open(file_path, 'r') as f:
    lines = f.readlines()
    for l in lines:
        sen = l.split()
        if len(sen) > 400:
            count += 1

print(count)


print(len(useless))