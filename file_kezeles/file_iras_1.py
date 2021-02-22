my_list = ['test', 'line']
with open('your_file.txt', 'w') as f:
    for item in my_list:
        f.write("%s\n" % item)
