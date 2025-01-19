from threading import *

class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat

    def reserve(self, need_seat):
        print('\nAvailable seats:', self.available_seat)
        if self.available_seat >= need_seat:
            name = current_thread().name  # Fixed method name: current_thread()
            print(f'{need_seat} seat(s) allotted for {name}\n')
            self.available_seat -= need_seat
        else:
            print("No seats available\n")

# Create a Flight object with 1 available seat
f = Flight(1)

# Create threads for different people trying to reserve seats
t1 = Thread(target=f.reserve, args=(1,), name='Rahul')
t2 = Thread(target=f.reserve, args=(1,), name='Sonam')

# Start the threads
t1.start()
t2.start()

# Join threads to ensure they finish execution before the program ends
t1.join()
t2.join()
