from time import perf_counter, sleep


class Timer:
    def __init__(self):
        self.start = perf_counter()

    def restart(self):
        self.start = perf_counter()

    def get_time(self):
        return perf_counter() - self.start

if __name__ == "__main__":
    my_timer = Timer()
    sleep(1)
    print(my_timer.get_time())