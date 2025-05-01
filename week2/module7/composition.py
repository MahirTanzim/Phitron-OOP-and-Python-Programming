class CPU:
    def __init__(self, cores):
        self.cores = cores

class RAM:
    def __init__(self, size):
        self.size = size

class HDD:
    def __init__(self, capacity):
        self.capacity = capacity


class PC:
    def __init__(self, cores, ram_size, hdd_capacity):
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hdd = HDD(hdd_capacity)
    

mac = PC(8, 16, 512)
print(mac.cpu.cores)