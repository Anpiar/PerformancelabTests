import statistics
import sys


def read_file(filename):
    with open(filename, 'r') as f:
        return list(map(int, f.read().split('\n')))


# Функция для вычисления перцентиля
def percentile(data):
    sorted_data = sorted(data)
    n = 0.9 * (len(sorted_data) - 1) + 1
    int_part = sorted_data[int(n) - 1]
    diff = sorted_data[int(n)] - int_part
    frac_part = (n % 1) * diff
    result = int_part + frac_part
    print('{:.2f}'.format(result))


if __name__ == '__main__':
    filename = sys.argv[1]
    mass = list(read_file(filename))
    if len(mass) > 1000:
        print('Файл содержит количество значений больше допустимого, обработаны будут первые 1000 значений' + '\n')
        data = mass[0:1000]  # делаем срез до 1000
    percentile(mass)
    print("{:.2f}".format(statistics.median(mass)))
    print("{:.2f}".format(max(mass)))
    print("{:.2f}".format(min(mass)))
    print("{:.2f}".format(statistics.mean(mass)))
