"""
Написать функцию host_range_ping_tab(), возможности которой
основаны на функции из примера 2. Но в данном случае результат
должен быть итоговым по всем ip-адресам, представленным в
табличном формате (использовать модуль tabulate).
"""
from subprocess import Popen, PIPE

from tabulate import tabulate


def host_range_ping(range_addr):
    start_addr = range_addr.split()[0].split('.')
    end_addr = range_addr.split()[2].split('.')
    result = {'Узел доступен': [], 'Узел недоступен': []}

    for addr in range(int(start_addr[3]), int(end_addr[3]) + 1):
        addr = start_addr[:3] + [str(addr)]
        addr = '.'.join(addr)
        args = ('ping', '-c', '1', addr)
        process = Popen(args, stdout=PIPE)
        process.wait()
        if process.returncode == 0:
            result['Узел доступен'].append(addr)
        else:
            result['Узел недоступен'].append(addr)

    print(tabulate(result, headers='keys', tablefmt='fancy_grid'))


host_range_ping('192.168.1.1 - 192.168.1.3')
