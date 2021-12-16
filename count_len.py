import os

file_path = os.path.join('data', 'bin_add_mult_expr_2e4', 'test_expr.txt')

useless = []

new_test_expr = os.path.join('data', 'bin_add_mult_expr_2e4', 'new_test_expr.txt')
new_expr = open(new_test_expr, 'w')
with open(file_path, 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        sen = lines[i].split()
        if len(sen) > 400:
            useless.append(i)
        else:
            new_expr.write(lines[i])
new_expr.close()

new_res_path = os.path.join('data', 'bin_add_mult_expr_2e4', 'new_test_res.txt')
new_res = open(new_res_path, 'w')
file_path = os.path.join('data', 'bin_add_mult_expr_2e4', 'test_res.txt')
with open(file_path, 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if i not in useless:
            new_res.write(lines[i])
new_res.close()

count = 0
file_path = os.path.join('data', 'bin_add_mult_expr_2e4', 'new_test_expr.txt')
with open(file_path, 'r') as f:
    lines = f.readlines()
    for l in lines:
        sen = l.split()
        if len(sen) > 400:
            count += 1

print(count)


print(len(useless))