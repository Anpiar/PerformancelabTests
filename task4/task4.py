import sys


def read_file(filename):
    with open(filename, 'r') as f:
        return list(map(float, f.read().replace(':', '.').replace('\n', ' ').split(' ')))


if __name__ == '__main__':
    filename = sys.argv[1]
    data = read_file(filename)
    times = [data[d:d + 2] for d in range(0, len(data), 2)]
    intervals = list(set(data))  # временные отметки без повторов
    intervals.sort()
    customers = []
    for i in range(len(intervals) - 1):
        customers.append(0)
        for j in range(len(times)):
            if times[j][0] <= intervals[i] < intervals[i + 1] <= times[j][1]:
                customers[i] += 1
    customers_pick = max(customers)
    for i in range(len(intervals) - 1):
        if customers_pick == customers[i] and (i == 0 or customers_pick != customers[i - 1]):
            result_time = '{:.2f}'.format(intervals[i]).replace('.', ':')
            print(result_time, end=' ')
        if customers_pick != customers[i] and customers_pick == customers[i - 1]:
            result_time = '{:.2f}'.format(intervals[i]).replace('.', ':')
            print(result_time)
