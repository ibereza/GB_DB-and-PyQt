"""
Написать функцию host_range_ping() для перебора ip-адресов
из заданного диапазона. Меняться должен только последний октет
каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""
from subprocess import Popen, PIPE


def host_range_ping(range_addr):
    start_addr = range_addr.split()[0].split('.')
    end_addr = range_addr.split()[2].split('.')

    for addr in range(int(start_addr[3]), int(end_addr[3]) + 1):
        addr = start_addr[:3] + [str(addr)]
        addr = '.'.join(addr)
        args = ('ping', '-c', '1', addr)
        process = Popen(args, stdout=PIPE)
        process.wait()
        if process.returncode == 0:
            print(f'{addr}: Узел доступен')
        else:
            print(f'{addr}: Узел недоступен')


host_range_ping('192.168.1.1 - 192.168.1.3')
