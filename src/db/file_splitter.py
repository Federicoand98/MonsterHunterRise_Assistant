def split_file(file_name, separator, out_folder):
    file = open(file_name, 'r')
    lines = file.readlines()

    count = 0
    for line in lines:
        name = out_folder + str(count) + '.txt'
        f = open(name, 'a')

        if line != separator:
            f.write(line)
        else:
            f.close()
            count = count + 1
