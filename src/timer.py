from time import perf_counter

TIME_UNITS = [
    ("seconds", 1),
    ("milliseconds", 1000),
    ("microseconds", 1000000)
]


def formatTime(time_in_seconds):
    for unit in TIME_UNITS:
        value = time_in_seconds * unit[1]
        if value >= 0.5:
            return f"{value:.4} {unit[0]}"

    return f"{time_in_seconds:.4} seconds"


class Timer:
    def __init__(self, operation_name):
        self.start_time = None
        self.operation_name = operation_name

    def __enter__(self):
        self.start_time = perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = perf_counter()
        print(f"{self.operation_name} took: {formatTime(end_time-self.start_time)}")

