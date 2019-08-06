with open(filename, 'r') as fp:
while True:
    cur_line = fp.readline()
#if the result is an emtry string
    if cur_lin == '':
#We have reached the end of the file
    break
print(cur_line)