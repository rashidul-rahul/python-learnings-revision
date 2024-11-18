import time
from functools import lru_cache

@lru_cache(maxsize=20)
def process_data(n):
    time.sleep(2)
    return n*n


start_time = time.time()
process_data(20)
print(f"first task taking time: {time.time() - start_time}")

start_time = time.time()
process_data(20)
print(f"second task taking time: {time.time() - start_time}")
