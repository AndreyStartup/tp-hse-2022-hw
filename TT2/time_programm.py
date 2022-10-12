import random
import Functions


def test_time_programm():
    count = 0
    while True:
        with open('test_file.txt', mode='w+') as fp:
            if count == 0:
                for i in range(1, 10):
                    number = random.randint(1, 100)
                    fp.write(f'{number} ')
                fp.seek(0)
                fp.read()
                fp.close()
                Functions.speed('test_file.txt')
                count += 1
            elif count == 1:
                for i in range(1, 100):
                    number = random.randint(1, 100)
                    fp.write(f'{number} ')
                fp.seek(0)
                fp.read()
                fp.close()
                Functions.speed('test_file.txt')
                count += 1
            elif count == 2:
                for i in range(1, 1000):
                    number = random.randint(1, 100)
                    fp.write(f'{number} ')
                fp.seek(0)
                fp.read()
                fp.close()
                Functions.speed('test_file.txt')
                count += 1
            elif count == 3:
                for i in range(1, 10000):
                    number = random.randint(1, 100)
                    fp.write(f'{number} ')
                fp.seek(0)
                fp.read()
                fp.close()
                Functions.speed('test_file.txt')
                count += 1
            elif count == 4:
                for i in range(1, 100000):
                    number = random.randint(1, 100)
                    fp.write(f'{number} ')
                fp.seek(0)
                fp.read()
                fp.close()
                Functions.speed('test_file.txt')
                count += 1
            elif count == 5:
                for i in range(1, 500000):
                    number = random.randint(1, 100)
                    fp.write(f'{number} ')
                fp.seek(0)
                fp.read()
                fp.close()
                Functions.speed('test_file.txt')
                count += 1
            elif count == 6:
                for i in range(1, 1000000):
                    number = random.randint(1, 100)
                    fp.write(f'{number} ')
                fp.seek(0)
                fp.read()
                fp.close()
                Functions.speed('test_file.txt')
                count += 1
            elif count == 7:
                break


test_time_programm()
