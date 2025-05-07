from abc import ABC, abstractmethod
import threading
import time

# Abstract
class DrivingStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass

# Конкретні 
class FastDrive(DrivingStrategy):
    def drive(self):
        print("Їдемо швидко — режим шосе.")

class EconomicDrive(DrivingStrategy):
    def drive(self):
        print("Їдемо економно — мінімальні витрати пального.")

class SafeDrive(DrivingStrategy):
    def drive(self):
        print("Їдемо обережно — безпечний режим у місті.")

# Контекст — транспортний засіб
class Vehicle:
    def __init__(self, name, strategy: DrivingStrategy):
        self.name = name
        self._strategy = strategy

    def set_strategy(self, strategy: DrivingStrategy):
        self._strategy = strategy

    def drive(self):
        print(f"{self.name}:", end=" ")
        self._strategy.drive()

# Функція для багатопотокового запуску
def drive_in_thread(vehicle):
    print(f"-> Потік {threading.current_thread().name} почав роботу")
    vehicle.drive()
    time.sleep(1)
    print(f"-> Потік {threading.current_thread().name} завершив роботу")

# Основна частина
if __name__ == "__main__":
    print("=== Однопоточна демонстрація ===")
    car = Vehicle("Легкове авто", FastDrive())
    truck = Vehicle("Фура", EconomicDrive())

    car.drive()
    truck.drive()

    # Зміна стратегії "на льоту"
    truck.set_strategy(SafeDrive())
    truck.drive()

    print("=== Багатопотокова демонстрація ===")
    vehicles = [
        Vehicle("Таксі", EconomicDrive()),
        Vehicle("Спорткар", FastDrive()),
        Vehicle("Вантажівка", SafeDrive())
    ]

    threads = []
    for v in vehicles:
        t = threading.Thread(target=drive_in_thread, args=(v,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
