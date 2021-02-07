import sys
import os.path


def read_file(filename):
    with open(filename, 'r') as f:
        return list(map(float, f.read().replace("\\n", "").split('\n')))


if __name__ == '__main__':
    directory = sys.argv[1]
    filenames = [os.path.join(directory, f'Cash{i}.txt') for i in range(1, 6)] # c os.path.join можно еще на Linux запустить :)
    cash_info = list(map(read_file, filenames))
    summary = list(map(sum, zip(*cash_info)))
    print(summary.index(max(summary)) + 1)
