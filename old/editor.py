def avava():
    file = open('дороги.txt', 'r', -1, 'utf-8')
    file2 = open('дороги test.txt', 'w', -1, 'utf-8')   
    dict_test = {}
    while True:
        line = file.readline()
        if not line: break
        else:
            if not ('8.107' in line): line_ = line
            file2.write(line_)
    file.close()
    file2.close()


avava()

