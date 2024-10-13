import random
import threading
import time
from queue import Queue
from threading import Thread
class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        waiting = random.randint(3, 10)
        time.sleep(waiting)
class Cafe:
    # list_thr = []
    list_guests = []

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        for i in range(len(self.tables)):
            self.tables[i].guest = guests[i]
            th1 = guests[i]
            th1.start()
            Cafe.list_guests.append(th1)
            print(f'{guests[i].name} сел(-а) за стол номер {self.tables[i].number}')
        if len(guests) > len (self.tables):
            for i in range(len(guests)):
                self.queue.put(guests[i])
                print(f'{guests[i].name} в очереди')
    def discuss_guests(self):
        while  not self.queue.empty() or



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
