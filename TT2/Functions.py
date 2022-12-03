import time
def read_from_file(Filename):
    array = []
    with open(Filename, 'r') as file:
        for line in file:
            array1 = line.split()
            for i in array1:
                array.append(int(i))
    return array


def _min(array):
    c = array[0]
    for i in array:
        if c>i:
            c = i
        else:
            continue
    return c


def _max(array):
    c = array[0]
    for i in array:
        if c<i:
            c = i
        else:
            continue
    return c


def _sum(array):
    count= 0
    for i in array:
        count +=i
    return count


def _mult(array):
    count = 1
    for i in array:
        count *=i
    return count

def speed(filename):
    start_time = time.time()
    array = read_from_file(filename)
    _min(array)
    _max(array)
    _sum(array)
    _mult(array)
    stop_time = time.time()
    print("Время работы:", stop_time - start_time, "сек")
