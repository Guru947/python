class computer1:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('config is', self.cpu, self.ram)


com1 = computer1('i5', 16)
com2 = computer1('ryzen', 8)

com1.config()
com2.config()
