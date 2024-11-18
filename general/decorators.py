import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"taking time: {end_time-start_time}")
        return result

    return wrapper


@time_decorator
def simple_sleep():
    time.sleep(1)

simple_sleep()