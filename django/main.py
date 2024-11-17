class Computer:
    def __init__(self, motherboard, processor, ram, storage):
        self.motherboard = motherboard
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def __str__(self):
        return f"Компьютер: \nМатеринская плата: {self.motherboard}\nПроцессор: {self.processor}\nОперативная память: {self.ram}\nХранилище: {self.storage}"


class ComputerBuilder:
    def __init__(self):
        self.motherboard = None
        self.processor = None
        self.ram = None
        self.storage = None

    def set_motherboard(self, motherboard):
        self.motherboard = motherboard
        return self  # Возвращаем себя для цепочечного вызова

    def set_processor(self, processor):
        self.processor = processor
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def build(self):
        return Computer(self.motherboard, self.processor, self.ram, self.storage)


computer_builder = ComputerBuilder()
computer = computer_builder \
    .set_motherboard("ASUS ROG Strix") \
    .set_processor("Intel Core i7") \
    .set_ram("16GB DDR4") \
    .set_storage("1TB SSD") \
    .build()

print(computer)