import Functions

def test_time_programm():
    count=0
    while True:
            with open('test_file.txt', mode='w+') as fp:
                if count == 0:
                    for i in range(1,10):
                        fp.write(f'{i} ')
                    fp.seek(0)
                    fp.read()
                    fp.close()
                    Functions.speed('test_file.txt')
                    count +=1
                elif count == 1:
                    for i in range(1,100):
                        fp.write(f'{i} ')
                    fp.seek(0)
                    fp.read()
                    fp.close()
                    Functions.speed('test_file.txt')
                    count +=1
                elif count == 2:
                    for i in range(1,1000):
                        fp.write(f'{i} ')
                    fp.seek(0)
                    fp.read()
                    fp.close()
                    Functions.speed('test_file.txt')
                    count +=1
                elif count == 3:
                    for i in range(1,10000):
                        fp.write(f'{i} ')
                    fp.seek(0)
                    fp.read()
                    fp.close()
                    Functions.speed('test_file.txt')
                    count +=1
                elif count == 4:
                    for i in range(1,100000):
                        fp.write(f'{i} ')
                    fp.seek(0)
                    fp.read()
                    fp.close()
                    Functions.speed('test_file.txt')
                    count +=1
                elif count == 5:
                    for i in range(1,500000):
                        fp.write(f'{i} ')
                    fp.seek(0)
                    fp.read()
                    fp.close()
                    Functions.speed('test_file.txt')
                    count +=1
                elif count == 6:
                    break


test_time_programm()