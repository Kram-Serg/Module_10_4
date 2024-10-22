import random
import time
from queue import Queue
from threading import Thread
class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        self.name_ = name
        super().__init__()

    def run(self):
        waiting = random.randint(3, 10)
        time.sleep(waiting)
class Cafe:

    list_guests = []

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables


    def guest_arrival(self, *guests):
        list_tables = self.tables
        for i in range(len(list_tables)):
            list_tables[i].guest = guests[i]
            thr = guests[i]
            thr.start()
            Cafe.list_guests.append(thr)
            print(f'{guests[i].name_} сел(-а) за стол номер {self.tables[i].number}')
        if len(guests) > len (list_tables):
            for i in range(len(list_tables),len(guests)):
                self.queue.put(guests[i])
                print(f'{guests[i].name_} в очереди')
    def discuss_guests(self):
        while not self.queue.empty() or Cafe.check_table(self):
            for table in self.tables:
                if not (table.guest is None) and not (table.guest.is_alive()):
                    print(f'{table.guest.name_} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name_} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    thr = table.guest
                    thr.start()
                    Cafe.list_guests.append(thr)

    def check_table(self):
        for table in self.tables:
            if table.guest is not None:
                return True
        return False

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

for thr in Cafe.list_guests:
    thr.join()
