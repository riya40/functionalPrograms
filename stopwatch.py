import time
"""
Printing the time lapsed using the stopwatch using the time function
"""


def time():
    input("Press Enter to start")
    start_time = time.time()

    input("Press Enter to stop")
    end_time = time.time()

    time_lapsed = end_time - start_time
    print(time_lapsed)


if __name__ == '__main__':
    time()
